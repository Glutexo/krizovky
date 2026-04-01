from django.test import TestCase
from django.urls import reverse

from .models import Tajenka


class TajenkaCrudTests(TestCase):
    def test_list_page_loads(self) -> None:
        response = self.client.get(reverse("tajenky:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tajenky")

    def test_create_tajenka(self) -> None:
        response = self.client.post(
            reverse("tajenky:create"),
            {"text": "JARO", "source_url": "https://example.com/jaro"},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        tajenka = Tajenka.objects.get(text="JARO")
        self.assertEqual(tajenka.source_url, "https://example.com/jaro")

    def test_update_tajenka(self) -> None:
        tajenka = Tajenka.objects.create(text="Léto")

        response = self.client.post(
            reverse("tajenky:update", args=[tajenka.pk]),
            {"text": "LÉTO", "source_url": "https://example.com/leto"},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        tajenka.refresh_from_db()
        self.assertEqual(tajenka.text, "LÉTO")
        self.assertEqual(tajenka.source_url, "https://example.com/leto")

    def test_delete_tajenka(self) -> None:
        tajenka = Tajenka.objects.create(text="ZIMA")

        response = self.client.post(reverse("tajenky:delete", args=[tajenka.pk]))

        self.assertRedirects(response, reverse("tajenky:list"))
        self.assertFalse(Tajenka.objects.filter(pk=tajenka.pk).exists())

    def test_source_url_is_optional(self) -> None:
        tajenka = Tajenka.objects.create(text="PODZIM")

        self.assertIsNone(tajenka.source_url)
