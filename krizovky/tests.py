from django.test import TestCase
from django.urls import reverse

from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerCrudTests(TestCase):
    def test_list_page_loads(self) -> None:
        response = self.client.get(reverse("krizovky:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tajenky")

    def test_create_answer(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/jaro")

        response = self.client.post(
            reverse("krizovky:create"),
            {"text": "JARO", "source_url": source_url.pk},
        )

        self.assertRedirects(response, reverse("krizovky:list"))
        answer = CrosswordAnswer.objects.get(text="JARO")
        self.assertEqual(answer.source_url, source_url)

    def test_update_answer(self) -> None:
        original_source_url = SourceURL.objects.create(url="https://example.com/leto-puvodni")
        new_source_url = SourceURL.objects.create(url="https://example.com/leto")
        answer = CrosswordAnswer.objects.create(text="Léto", source_url=original_source_url)

        response = self.client.post(
            reverse("krizovky:update", args=[answer.pk]),
            {"text": "LÉTO", "source_url": new_source_url.pk},
        )

        self.assertRedirects(response, reverse("krizovky:list"))
        answer.refresh_from_db()
        self.assertEqual(answer.text, "LÉTO")
        self.assertEqual(answer.source_url, new_source_url)

    def test_create_answer_without_source_url(self) -> None:
        response = self.client.post(
            reverse("krizovky:create"),
            {"text": "LISTOPAD", "source_url": ""},
        )

        self.assertRedirects(response, reverse("krizovky:list"))
        answer = CrosswordAnswer.objects.get(text="LISTOPAD")
        self.assertIsNone(answer.source_url)

    def test_delete_answer(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/zima")
        answer = CrosswordAnswer.objects.create(text="ZIMA", source_url=source_url)

        response = self.client.post(reverse("krizovky:delete", args=[answer.pk]))

        self.assertRedirects(response, reverse("krizovky:list"))
        self.assertFalse(CrosswordAnswer.objects.filter(pk=answer.pk).exists())
        self.assertIsNotNone(CrosswordAnswer.all_objects.get(pk=answer.pk).deleted_at)

    def test_source_url_can_have_multiple_answers(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/spolecny-zdroj")
        CrosswordAnswer.objects.create(text="PODZIM", source_url=source_url)
        CrosswordAnswer.objects.create(text="JARO", source_url=source_url)

        self.assertEqual(source_url.answers.count(), 2)

    def test_update_answer_can_clear_source_url(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/docasny-zdroj")
        answer = CrosswordAnswer.objects.create(text="DUBEN", source_url=source_url)

        response = self.client.post(
            reverse("krizovky:update", args=[answer.pk]),
            {"text": "DUBEN", "source_url": ""},
        )

        self.assertRedirects(response, reverse("krizovky:list"))
        answer.refresh_from_db()
        self.assertIsNone(answer.source_url)

    def test_deleted_answer_is_hidden_from_list(self) -> None:
        answer = CrosswordAnswer.objects.create(text="SKRYTA")
        answer.soft_delete()

        response = self.client.get(reverse("krizovky:list"))

        self.assertNotContains(response, "SKRYTA")


class SourceURLCrudTests(TestCase):
    def test_list_page_loads(self) -> None:
        response = self.client.get(reverse("krizovky:source_url_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "URL zdroje")

    def test_create_source_url(self) -> None:
        response = self.client.post(
            reverse("krizovky:source_url_create"),
            {"url": "https://example.com/novy-zdroj"},
        )

        self.assertRedirects(response, reverse("krizovky:source_url_list"))
        self.assertTrue(SourceURL.objects.filter(url="https://example.com/novy-zdroj").exists())

    def test_update_source_url(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/stary-zdroj")

        response = self.client.post(
            reverse("krizovky:source_url_update", args=[source_url.pk]),
            {"url": "https://example.com/novy-zdroj"},
        )

        self.assertRedirects(response, reverse("krizovky:source_url_list"))
        source_url.refresh_from_db()
        self.assertEqual(source_url.url, "https://example.com/novy-zdroj")

    def test_delete_unused_source_url(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/smazat-zdroj")

        response = self.client.post(
            reverse("krizovky:source_url_delete", args=[source_url.pk]),
        )

        self.assertRedirects(response, reverse("krizovky:source_url_list"))
        self.assertFalse(SourceURL.objects.filter(pk=source_url.pk).exists())
        self.assertIsNotNone(SourceURL.all_objects.get(pk=source_url.pk).deleted_at)

    def test_deleted_source_url_is_hidden_from_picker(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/skryty-zdroj")
        source_url.soft_delete()

        response = self.client.get(reverse("krizovky:create"))

        self.assertNotContains(response, source_url.url)

    def test_creating_same_deleted_source_url_restores_it(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/obnovit-zdroj")
        source_url.soft_delete()

        response = self.client.post(
            reverse("krizovky:source_url_create"),
            {"url": source_url.url},
        )

        self.assertRedirects(response, reverse("krizovky:source_url_list"))
        source_url.refresh_from_db()
        self.assertIsNone(source_url.deleted_at)
