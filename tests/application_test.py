from unittest import TestCase
from app.application import Application


class ApplicationTest(TestCase):
    def test_say_Hello(self):
        # Given
        application = Application()
        expected = "Hello"
        # When
        result = application.say_hello()
        # Then
        self.assertEqual(expected, result)
