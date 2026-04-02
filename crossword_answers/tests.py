from django.test import TestCase
from django.urls import reverse

from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerCrudTests(TestCase):
    def test_list_page_loads(self) -> None:
        response = self.client.get(reverse("crossword_answers:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tajenky")

    def test_create_answer(self) -> None:
        response = self.client.post(
            reverse("crossword_answers:create"),
            {"text": "JARO", "source_url_value": "https://example.com/jaro"},
        )

        self.assertRedirects(response, reverse("crossword_answers:list"))
        answer = CrosswordAnswer.objects.get(text="JARO")
        self.assertEqual(answer.source_url.url, "https://example.com/jaro")

    def test_update_answer(self) -> None:
        original_source_url = SourceURL.objects.create(url="https://example.com/leto-puvodni")
        answer = CrosswordAnswer.objects.create(text="Léto", source_url=original_source_url)

        response = self.client.post(
            reverse("crossword_answers:update", args=[answer.pk]),
            {"text": "LÉTO", "source_url_value": "https://example.com/leto"},
        )

        self.assertRedirects(response, reverse("crossword_answers:list"))
        answer.refresh_from_db()
        self.assertEqual(answer.text, "LÉTO")
        self.assertEqual(answer.source_url.url, "https://example.com/leto")

    def test_delete_answer(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/zima")
        answer = CrosswordAnswer.objects.create(text="ZIMA", source_url=source_url)

        response = self.client.post(reverse("crossword_answers:delete", args=[answer.pk]))

        self.assertRedirects(response, reverse("crossword_answers:list"))
        self.assertFalse(CrosswordAnswer.objects.filter(pk=answer.pk).exists())

    def test_source_url_can_have_multiple_answers(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/spolecny-zdroj")
        CrosswordAnswer.objects.create(text="PODZIM", source_url=source_url)
        CrosswordAnswer.objects.create(text="JARO", source_url=source_url)

        self.assertEqual(source_url.answers.count(), 2)

    def test_existing_source_url_is_reused(self) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/opakovany-zdroj")

        response = self.client.post(
            reverse("crossword_answers:create"),
            {"text": "SRPEN", "source_url_value": source_url.url},
        )

        self.assertRedirects(response, reverse("crossword_answers:list"))
        self.assertEqual(SourceURL.objects.filter(url=source_url.url).count(), 1)
