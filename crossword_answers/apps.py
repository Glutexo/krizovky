from django.apps import AppConfig


class CrosswordAnswersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crossword_answers"
    label = "tajenky"

    def ready(self) -> None:
        from . import checks  # noqa: F401
