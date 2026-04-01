from django.conf import settings
from openai import OpenAI


class OpenAIConfigurationError(RuntimeError):
    """Vyhozena pri chybejici konfiguraci OpenAI."""


def is_plausible_openai_api_key(api_key: str) -> bool:
    stripped_key = api_key.strip()
    return stripped_key.startswith("sk-") and len(stripped_key) >= 20 and "\n" not in stripped_key


def build_openai_client(*, api_key: str) -> OpenAI:
    if not api_key:
        raise OpenAIConfigurationError(
            "Chybí OPENAI_API_KEY. Nastav proměnnou prostředí nebo hodnotu v .env."
        )

    if not is_plausible_openai_api_key(api_key):
        raise OpenAIConfigurationError(
            "OPENAI_API_KEY nevypadá jako platný OpenAI klíč. Zkontroluj hodnotu v prostředí nebo v .env."
        )

    return OpenAI(api_key=api_key)


def get_openai_client() -> OpenAI:
    return build_openai_client(api_key=settings.OPENAI_API_KEY)
