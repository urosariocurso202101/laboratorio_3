import unittest

from calculadora import suma


class CalculadoraTest(unittest.TestCase):

    def setUp(self) -> None:
        self.numero1 = 2
        self.numero2 = 2

    def test_suma_ok(self):
        resultado = suma(self.numero2, self.numero1)
        self.assertEqual(resultado, self.numero2 + self.numero1)
