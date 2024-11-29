#!./venv/bin/python
import unittest
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, get_true_distance, get_false_distance

def distancia_palabra_operador(palabra, operador):
    return min((abs(ord(x) - ord(operador)) for x in palabra))

class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):

    # En cada Test analizamos el diccionario de distancias comprobando que cada distancia
    # esté correctamente calculada luego de ejecutar cgi_decode_instrumented

    # Palabra vacía
    def testEmpty(self):
        clear_maps()
        self.assertEqual(cgi_decode_instrumented(""), "")
        self.assertEqual(get_true_distance(1), 1)
        self.assertEqual(get_false_distance(1), 0)
        
        self.assertIsNone(get_true_distance(2))
        self.assertIsNone(get_false_distance(2))

        self.assertIsNone(get_true_distance(3))
        self.assertIsNone(get_false_distance(3))

        self.assertIsNone(get_true_distance(4))
        self.assertIsNone(get_false_distance(4))

        self.assertIsNone(get_true_distance(5))
        self.assertIsNone(get_false_distance(5))


    # Sin codificación
    def testNoEncoding(self):
        clear_maps()

        self.assertEqual(cgi_decode_instrumented("Hello World"), "Hello World")
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_false_distance(1), 0)
        
        self.assertEqual(get_true_distance(2), 11)
        self.assertEqual(get_false_distance(2), 0)

        self.assertEqual(get_true_distance(3), 5)
        self.assertEqual(get_false_distance(3), 0)

        self.assertIsNone(get_true_distance(4))
        self.assertIsNone(get_false_distance(4))

        self.assertIsNone(get_true_distance(5))
        self.assertIsNone(get_false_distance(5))

        


    # Con +
    def testPlus(self):
        clear_maps()

        self.assertEqual(cgi_decode_instrumented("Hello+World"), "Hello World")
        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_false_distance(1), 0)
        
        self.assertEqual(get_true_distance(2), 0)
        self.assertEqual(get_false_distance(2), 0)

        self.assertEqual(get_true_distance(3), 35)
        self.assertEqual(get_false_distance(3), 0)

        self.assertIsNone(get_true_distance(4))
        self.assertIsNone(get_false_distance(4))

        self.assertIsNone(get_true_distance(5))
        self.assertIsNone(get_false_distance(5))

    # Con %
    def testPercent(self):
        clear_maps()
        self.assertEqual(cgi_decode_instrumented("Hello%20World"), "Hello World")

        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_false_distance(1), 0)
        
        self.assertEqual(get_true_distance(2), 6)
        self.assertEqual(get_false_distance(2), 0)

        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_false_distance(3), 0)

        self.assertEqual(get_true_distance(4), 0)
        self.assertEqual(get_false_distance(4), 1)

        self.assertEqual(get_true_distance(5), 0)
        self.assertEqual(get_false_distance(5), 1)


    # Digit low no es un dígito hexadecimal
    def testInvalidDigitLow(self):
        clear_maps()
        with self.assertRaises(ValueError):
            cgi_decode_instrumented("Hello%2GWorld")

        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_false_distance(1), 8)
        
        self.assertEqual(get_true_distance(2),6 )
        self.assertEqual(get_false_distance(2),0 ) 

        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_false_distance(3), 0)

        self.assertEqual(get_true_distance(4), 0)
        self.assertEqual(get_false_distance(4), 1)

        self.assertEqual(get_true_distance(5), 1)
        self.assertEqual(get_false_distance(5), 0)



    # Digit high no es un dígito hexadecimal
    def testInvalidDigitHigh(self):
        clear_maps()
        with self.assertRaises(ValueError):
            cgi_decode_instrumented("Hello%G2World")


        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_false_distance(1), 8)
        
        self.assertEqual(get_true_distance(2), 6)
        self.assertEqual(get_false_distance(2), 0) 

        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_false_distance(3), 0)

        self.assertEqual(get_true_distance(4), 1)
        self.assertEqual(get_false_distance(4), 0)

        self.assertIsNone(get_true_distance(5))
        self.assertIsNone(get_false_distance(5))

    