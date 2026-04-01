from django.conf import settings
from openai import OpenAI


class OpenAIConfigurationError(RuntimeError):
    """Vyhozena pri chybejici konfiguraci OpenAI."""


def build_openai_client(*, api_key: str) -> OpenAI:
    if not api_key:
        raise OpenAIConfigurationError(
            "Chybí OPENAI_API_KEY. Nastav proměnnou prostředí nebo hodnotu v .env."
        )

    return OpenAI(api_key=api_key)


def get_openai_client() -> OpenAI:
    return build_openai_client(api_key=settings.OPENAI_API_KEY)
