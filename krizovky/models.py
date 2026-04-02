from django.db import models
from django.utils import timezone


class VisibilityQuerySet(models.QuerySet):
    def active(self):
        return self.filter(hidden_at__isnull=True)

    def hidden(self):
        return self.filter(hidden_at__isnull=False)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return VisibilityQuerySet(self.model, using=self._db).active()


class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return VisibilityQuerySet(self.model, using=self._db)


class SourceURL(models.Model):
    url = models.URLField("Zdrojová URL", unique=True)
    created_at = models.DateTimeField("Vytvořeno", auto_now_add=True)
    updated_at = models.DateTimeField("Upraveno", auto_now=True)
    hidden_at = models.DateTimeField("Skryto", blank=True, null=True)

    objects = ActiveManager()
    all_objects = AllObjectsManager()

    class Meta:
        db_table = "crossword_answers_source_url"
        ordering = ["url"]
        verbose_name = "zdrojová URL"
        verbose_name_plural = "zdrojové URL"

    def __str__(self) -> str:
        return self.url

    def hide(self) -> None:
        self.hidden_at = timezone.now()
        self.save(update_fields=["hidden_at", "updated_at"])

    def restore(self) -> None:
        self.hidden_at = None
        self.save(update_fields=["hidden_at", "updated_at"])


class CrosswordAnswer(models.Model):
    text = models.CharField("Tajenka", max_length=255)
    source_url = models.ForeignKey(
        SourceURL,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="answers",
        verbose_name="Zdrojová URL",
    )
    created_at = models.DateTimeField("Vytvořeno", auto_now_add=True)
    updated_at = models.DateTimeField("Upraveno", auto_now=True)
    hidden_at = models.DateTimeField("Skryto", blank=True, null=True)

    objects = ActiveManager()
    all_objects = AllObjectsManager()

    class Meta:
        db_table = "crossword_answers_crossword_answer"
        ordering = ["text"]
        verbose_name = "tajenka"
        verbose_name_plural = "tajenky"

    def __str__(self) -> str:
        return self.text

    def hide(self) -> None:
        self.hidden_at = timezone.now()
        self.save(update_fields=["hidden_at", "updated_at"])

    def restore(self) -> None:
        self.hidden_at = None
        self.save(update_fields=["hidden_at", "updated_at"])
