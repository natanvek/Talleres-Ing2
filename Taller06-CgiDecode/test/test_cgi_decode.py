#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode


class TestCgiDecode(unittest.TestCase):

    # Palabra vacía
    def testEmpty(self):
        self.assertEqual(cgi_decode(""), "")

    # Sin codificación
    def testNoEncoding(self):
        self.assertEqual(cgi_decode("Hello World"), "Hello World")

    # Con +
    def testPlus(self):
        self.assertEqual(cgi_decode("Hello+World"), "Hello World")

    # Con %
    def testPercent(self):
        self.assertEqual(cgi_decode("Hello%20World"), "Hello World")

    # Digit low no es un dígito hexadecimal
    def testInvalidDigitLow(self):
        with self.assertRaises(ValueError):
            cgi_decode("Hello%2GWorld")

    # Digit high no es un dígito hexadecimal
    def testInvalidDigitHigh(self):
        with self.assertRaises(ValueError):
            cgi_decode("Hello%G2World")

    