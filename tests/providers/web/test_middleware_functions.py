import unittest

from providers.web.fastapi.exceptions import MissingHeaderException
from providers.web.middleware_functions import infer_user_language_from_header


class TestInferUserLanguageFromHeader(unittest.TestCase):
    def test_with_empty_string(self):
        with self.assertRaises(MissingHeaderException):
            infer_user_language_from_header('')

    def test_with_none(self):
        with self.assertRaises(MissingHeaderException):
            infer_user_language_from_header(None)

    def test_get_language_with_the_highest_confidence_score(self):
        header_value = 'en-GB,en-US;q=0.9,fr-CA;q=0.7,en;q=0.8'

        language = infer_user_language_from_header(header_value)

        self.assertEqual(language, 'en-GB')


if __name__ == '__main__':
    unittest.main()
