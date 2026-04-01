from django.conf import settings
from django.core.checks import Warning, register

from .openai_client import is_plausible_openai_api_key


@register()
def openai_configuration_check(app_configs, **kwargs):
    if not settings.OPENAI_API_KEY:
        return [
            Warning(
                "OpenAI API klíč není nastavený.",
                hint="Doplň OPENAI_API_KEY do proměnné prostředí nebo do lokálního souboru .env.",
                id="tajenky.W001",
            )
        ]

    if not is_plausible_openai_api_key(settings.OPENAI_API_KEY):
        return [
            Warning(
                "OpenAI API klíč má neobvyklý formát.",
                hint="Zkontroluj, že OPENAI_API_KEY nezačíná nebo nekončí navíc uvozovkami a není zkrácený.",
                id="tajenky.W002",
            )
        ]

    return []
