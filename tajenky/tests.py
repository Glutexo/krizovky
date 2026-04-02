from django.test import TestCase
from django.urls import reverse

from .models import Tajenka, ZdrojovaURL


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
        self.assertEqual(tajenka.source.url, "https://example.com/jaro")

    def test_update_tajenka(self) -> None:
        original_source = ZdrojovaURL.objects.create(url="https://example.com/leto-puvodni")
        tajenka = Tajenka.objects.create(text="Léto", source=original_source)

        response = self.client.post(
            reverse("tajenky:update", args=[tajenka.pk]),
            {"text": "LÉTO", "source_url": "https://example.com/leto"},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        tajenka.refresh_from_db()
        self.assertEqual(tajenka.text, "LÉTO")
        self.assertEqual(tajenka.source.url, "https://example.com/leto")

    def test_delete_tajenka(self) -> None:
        source = ZdrojovaURL.objects.create(url="https://example.com/zima")
        tajenka = Tajenka.objects.create(text="ZIMA", source=source)

        response = self.client.post(reverse("tajenky:delete", args=[tajenka.pk]))

        self.assertRedirects(response, reverse("tajenky:list"))
        self.assertFalse(Tajenka.objects.filter(pk=tajenka.pk).exists())

    def test_source_can_have_multiple_tajenky(self) -> None:
        source = ZdrojovaURL.objects.create(url="https://example.com/spolecny-zdroj")
        Tajenka.objects.create(text="PODZIM", source=source)
        Tajenka.objects.create(text="JARO", source=source)

        self.assertEqual(source.tajenky.count(), 2)

    def test_existing_source_url_is_reused(self) -> None:
        source = ZdrojovaURL.objects.create(url="https://example.com/opakovany-zdroj")

        response = self.client.post(
            reverse("tajenky:create"),
            {"text": "SRPEN", "source_url": source.url},
        )

        self.assertRedirects(response, reverse("tajenky:list"))
        self.assertEqual(ZdrojovaURL.objects.filter(url=source.url).count(), 1)
