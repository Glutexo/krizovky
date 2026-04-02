from unittest.mock import Mock, patch

from django.test import SimpleTestCase, TestCase, override_settings

from .models import CrosswordAnswer, SourceURL
from .source_import import extract_answers_from_source, import_answers_from_source_url, parse_answers_payload


class SourceImportParsingTests(SimpleTestCase):
    def test_parse_answers_payload_accepts_plain_json_array(self) -> None:
        answers = parse_answers_payload('["Praha", "Brno", "Praha"]')

        self.assertEqual(answers, ["PRAHA", "BRNO"])

    def test_parse_answers_payload_accepts_answers_object(self) -> None:
        answers = parse_answers_payload('{"answers": ["Nový rok", "Sníh"]}')

        self.assertEqual(answers, ["NOVÝ ROK", "SNÍH"])

    @override_settings(OPENAI_API_KEY="sk-test-12345678901234567890", OPENAI_MODEL="gpt-4.1-mini")
    @patch("krizovky.source_import.fetch_source_text", return_value="Praha je hlavní město.")
    @patch("krizovky.source_import.get_openai_client")
    def test_extract_answers_from_source_uses_openai_response(self, get_client_mock, fetch_text_mock) -> None:
        client = Mock()
        client.responses.create.return_value.output_text = '["Praha", "Karlův most"]'
        get_client_mock.return_value = client

        answers = extract_answers_from_source("https://example.com/praha")

        self.assertEqual(answers, ["PRAHA", "KARLŮV MOST"])
        fetch_text_mock.assert_called_once_with("https://example.com/praha")
        client.responses.create.assert_called_once()


class SourceImportPersistenceTests(TestCase):
    @patch("krizovky.source_import.extract_answers_from_source", return_value=["PRAHA", "BRNO"])
    def test_import_answers_creates_source_and_answers(self, extract_mock) -> None:
        result = import_answers_from_source_url("https://example.com/mesta")

        self.assertEqual(result.created_count, 2)
        self.assertEqual(result.restored_count, 0)
        self.assertEqual(result.skipped_count, 0)
        self.assertTrue(SourceURL.objects.filter(url="https://example.com/mesta").exists())
        self.assertEqual(CrosswordAnswer.objects.filter(source_url__url="https://example.com/mesta").count(), 2)
        extract_mock.assert_called_once_with("https://example.com/mesta")

    @patch("krizovky.source_import.extract_answers_from_source", return_value=["PRAHA", "BRNO"])
    def test_import_answers_restores_hidden_records_and_skips_duplicates(self, extract_mock) -> None:
        source_url = SourceURL.objects.create(url="https://example.com/mesta")
        hidden_answer = CrosswordAnswer.objects.create(text="PRAHA", source_url=source_url)
        visible_answer = CrosswordAnswer.objects.create(text="BRNO", source_url=source_url)
        source_url.hide()
        hidden_answer.hide()

        result = import_answers_from_source_url(source_url.url)

        self.assertEqual(result.created_count, 0)
        self.assertEqual(result.restored_count, 1)
        self.assertEqual(result.skipped_count, 1)
        source_url.refresh_from_db()
        hidden_answer.refresh_from_db()
        visible_answer.refresh_from_db()
        self.assertIsNone(source_url.hidden_at)
        self.assertIsNone(hidden_answer.hidden_at)
        self.assertIsNone(visible_answer.hidden_at)
        extract_mock.assert_called_once_with(source_url.url)
