from django.apps import AppConfig


class KrizovkyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "krizovky"
    label = "tajenky"

    def ready(self) -> None:
        from . import checks  # noqa: F401
