import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.conf import settings
from openai import APIConnectionError, APIStatusError, APITimeoutError, RateLimitError

from .models import CrosswordAnswer, SourceURL
from .openai_client import OpenAIConfigurationError, get_openai_client


class SourceImportError(RuntimeError):
    """Chyba pri importu tajenek ze zdrojove URL."""


@dataclass(frozen=True)
class ImportResult:
    source_url: SourceURL
    created_count: int
    restored_count: int
    skipped_count: int


def build_openai_api_error_message(exc: Exception) -> str:
    if isinstance(exc, RateLimitError):
        error_body = exc.body if isinstance(exc.body, dict) else {}
        error_code = error_body.get("code")

        if error_code == "insufficient_quota":
            return "AI import teď není dostupný, protože OpenAI účet nemá dostatečnou kvótu."

        return "AI import je dočasně omezený kvůli limitu OpenAI API. Zkus to prosím znovu později."

    if isinstance(exc, APITimeoutError):
        return "OpenAI API neodpovědělo včas. Zkus to prosím znovu."

    if isinstance(exc, APIConnectionError):
        return "Nepodařilo se spojit s OpenAI API. Zkontroluj připojení a zkus to znovu."

    if isinstance(exc, APIStatusError):
        return f"OpenAI API vrátilo chybu {exc.status_code}. Zkus to prosím znovu později."

    return "AI import se nepodařilo dokončit kvůli chybě OpenAI API."


class HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.chunks: list[str] = []
        self.ignored_tags = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "noscript"}:
            self.ignored_tags += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.ignored_tags:
            self.ignored_tags -= 1

    def handle_data(self, data: str) -> None:
        if self.ignored_tags:
            return

        text = " ".join(data.split())
        if text:
            self.chunks.append(text)

    def get_text(self) -> str:
        return " ".join(self.chunks)


def fetch_source_text(url: str, *, max_bytes: int = 250_000, max_chars: int = 12_000) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "krizovky-bot/0.1 (+https://github.com/Glutexo/krizovky)",
        },
    )

    try:
        with urlopen(request, timeout=15) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            html = response.read(max_bytes).decode(charset, errors="replace")
    except HTTPError as exc:
        raise SourceImportError(f"Zdrojovou stránku se nepodařilo načíst. Server vrátil HTTP {exc.code}.") from exc
    except URLError as exc:
        raise SourceImportError("Zdrojovou stránku se nepodařilo načíst. Zkontroluj URL a dostupnost serveru.") from exc

    extractor = HTMLTextExtractor()
    extractor.feed(html)
    text = extractor.get_text()

    if not text:
        raise SourceImportError("Na zdrojové stránce se nepodařilo najít čitelný text pro analýzu.")

    return text[:max_chars]


def parse_answers_payload(payload: str) -> list[str]:
    normalized_payload = payload.strip()
    if normalized_payload.startswith("```"):
        normalized_payload = re.sub(r"^```(?:json)?\s*", "", normalized_payload)
        normalized_payload = re.sub(r"\s*```$", "", normalized_payload)

    try:
        data = json.loads(normalized_payload)
    except json.JSONDecodeError as exc:
        raise SourceImportError("OpenAI nevrátilo validní JSON se seznamem tajenek.") from exc

    if isinstance(data, dict):
        data = data.get("answers", [])

    if not isinstance(data, list):
        raise SourceImportError("OpenAI nevrátilo seznam tajenek v očekávaném formátu.")

    unique_answers: list[str] = []
    seen: set[str] = set()

    for raw_answer in data:
        if not isinstance(raw_answer, str):
            continue

        answer = " ".join(raw_answer.split()).strip(" ,.;:-").upper()
        if not answer or answer in seen:
            continue

        seen.add(answer)
        unique_answers.append(answer)

    if not unique_answers:
        raise SourceImportError("OpenAI nenašlo žádné použitelné tajenky.")

    return unique_answers


def extract_answers_from_source(url: str) -> list[str]:
    source_text = fetch_source_text(url)

    try:
        client = get_openai_client()
    except OpenAIConfigurationError as exc:
        raise SourceImportError(str(exc)) from exc

    try:
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[
                {
                    "role": "system",
                    "content": (
                        "Z poskytnutého textu vybírej krátké, srozumitelné a samostatně použitelné tajenky do křížovek. "
                        "Vrať pouze JSON pole řetězců bez dalšího komentáře. "
                        "Používej velká písmena, maximálně 3 slova na položku a nevracej celé věty."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Zdrojová URL: {url}\n"
                        "Vyber z následujícího textu vhodné tajenky do křížovek:\n\n"
                        f"{source_text}"
                    ),
                },
            ],
        )
    except (APIConnectionError, APIStatusError, APITimeoutError, RateLimitError) as exc:
        raise SourceImportError(build_openai_api_error_message(exc)) from exc

    return parse_answers_payload(response.output_text)


def get_or_create_source_url(url: str) -> SourceURL:
    source_url = SourceURL.all_objects.filter(url=url).first()
    if source_url is None:
        return SourceURL.objects.create(url=url)

    if source_url.hidden_at is not None:
        source_url.restore()

    return source_url


def import_answers_from_source_url(url: str) -> ImportResult:
    source_url = get_or_create_source_url(url)
    answers = extract_answers_from_source(url)

    created_count = 0
    restored_count = 0
    skipped_count = 0

    for answer_text in answers:
        existing = CrosswordAnswer.all_objects.filter(text=answer_text, source_url=source_url).first()
        if existing is None:
            CrosswordAnswer.objects.create(text=answer_text, source_url=source_url)
            created_count += 1
            continue

        if existing.hidden_at is not None:
            existing.restore()
            restored_count += 1
            continue

        skipped_count += 1

    return ImportResult(
        source_url=source_url,
        created_count=created_count,
        restored_count=restored_count,
        skipped_count=skipped_count,
    )
