from django.test import SimpleTestCase, override_settings

from .checks import openai_configuration_check
from .openai_client import is_plausible_openai_api_key


class OpenAIConfigurationChecksTests(SimpleTestCase):
    @override_settings(OPENAI_API_KEY="")
    def test_check_warns_when_key_is_missing(self) -> None:
        messages = openai_configuration_check(None)

        self.assertEqual([message.id for message in messages], ["crossword_answers.W001"])

    @override_settings(OPENAI_API_KEY="invalid-key")
    def test_check_warns_when_key_has_invalid_format(self) -> None:
        messages = openai_configuration_check(None)

        self.assertEqual([message.id for message in messages], ["crossword_answers.W002"])

    @override_settings(OPENAI_API_KEY="sk-test-12345678901234567890")
    def test_check_passes_for_plausible_key(self) -> None:
        messages = openai_configuration_check(None)

        self.assertEqual(messages, [])


class OpenAIKeyValidationTests(SimpleTestCase):
    def test_key_validation_accepts_plausible_key(self) -> None:
        self.assertTrue(is_plausible_openai_api_key("sk-test-12345678901234567890"))

    def test_key_validation_rejects_short_value(self) -> None:
        self.assertFalse(is_plausible_openai_api_key("sk-short"))
