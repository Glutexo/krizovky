from django.test import SimpleTestCase, override_settings

from .openai_client import OpenAIConfigurationError, build_openai_client


class OpenAIClientTests(SimpleTestCase):
    @override_settings(OPENAI_API_KEY="")
    def test_build_client_requires_api_key(self) -> None:
        with self.assertRaises(OpenAIConfigurationError):
            build_openai_client(api_key="")

    def test_build_client_accepts_api_key(self) -> None:
        client = build_openai_client(api_key="test-key")

        self.assertEqual(client.api_key, "test-key")
