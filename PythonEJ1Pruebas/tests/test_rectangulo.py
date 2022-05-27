import unittest 
from poligonos.Rectangulo import area_rectangulo

class TestRectangulo(unittest.TestCase):

    def test_area_rectangulo_entero(self):
        base = 2
        altura = 4
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(area, 8)

    def test_area_rectangulo_flotante(self):
        base = 2
        altura = 2.3412
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(area, 4,6824)

    def test_area_rectangulo_invalida(self):
        base = 'hola'
        altura = 4
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(str(exc.exception), "La base debe ser del tipo real")

    def test_area_rectangulo_invalida(self):
        base = 4
        altura = 'hola'
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(str(exc.exception), "La altura debe ser del tipo real")

    def test_area_rectangulo_invalida(self):
        base = -1
        altura = 4
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(str(exc.exception), "La base debe ser positiva")

    def test_area_rectangulo_invalida(self):
        base = 4
        altura = -1
        area = area_rectangulo(base = base, altura = altura)
        self.assertEqual(str(exc.exception), "La altura debe ser positiva")

if __name__ == '__main__':
    unittest.main()