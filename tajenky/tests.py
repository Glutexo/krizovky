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
            {"text": "JARO"},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        self.assertTrue(Tajenka.objects.filter(text="JARO").exists())

    def test_update_tajenka(self) -> None:
        tajenka = Tajenka.objects.create(text="Léto")

        response = self.client.post(
            reverse("tajenky:update", args=[tajenka.pk]),
            {"text": "LÉTO"},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        tajenka.refresh_from_db()
        self.assertEqual(tajenka.text, "LÉTO")

    def test_delete_tajenka(self) -> None:
        tajenka = Tajenka.objects.create(text="ZIMA")

        response = self.client.post(reverse("tajenky:delete", args=[tajenka.pk]))

        self.assertRedirects(response, reverse("tajenky:list"))
        self.assertFalse(Tajenka.objects.filter(pk=tajenka.pk).exists())
