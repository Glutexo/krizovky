from django.apps import AppConfig


class TajenkyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'tajenky'

    def ready(self) -> None:
        from . import checks  # noqa: F401
