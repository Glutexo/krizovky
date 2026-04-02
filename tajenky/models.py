from django.db import models


class ZdrojovaURL(models.Model):
    url = models.URLField("Zdrojová URL", unique=True)
    created_at = models.DateTimeField("Vytvořeno", auto_now_add=True)
    updated_at = models.DateTimeField("Upraveno", auto_now=True)

    class Meta:
        ordering = ["url"]
        verbose_name = "zdrojová URL"
        verbose_name_plural = "zdrojové URL"

    def __str__(self) -> str:
        return self.url


class Tajenka(models.Model):
    text = models.CharField("Tajenka", max_length=255)
    source = models.ForeignKey(
        ZdrojovaURL,
        on_delete=models.PROTECT,
        related_name="tajenky",
        verbose_name="Zdrojová URL",
    )
    created_at = models.DateTimeField("Vytvořeno", auto_now_add=True)
    updated_at = models.DateTimeField("Upraveno", auto_now=True)

    class Meta:
        ordering = ["text"]
        verbose_name = "tajenka"
        verbose_name_plural = "tajenky"

    def __str__(self) -> str:
        return self.text
