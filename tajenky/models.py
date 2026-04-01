from django.db import models


class Tajenka(models.Model):
    text = models.CharField("Tajenka", max_length=255)
    source_url = models.URLField("Zdrojová URL", blank=True, null=True)
    created_at = models.DateTimeField("Vytvořeno", auto_now_add=True)
    updated_at = models.DateTimeField("Upraveno", auto_now=True)

    class Meta:
        ordering = ["text"]
        verbose_name = "tajenka"
        verbose_name_plural = "tajenky"

    def __str__(self) -> str:
        return self.text
