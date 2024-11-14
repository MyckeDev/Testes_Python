from calculadoraIMC  import CalculadoraIMC  # Use the correct class name with uppercase C
import unittest

class TestCalculadoraIMC(unittest.TestCase):
    
    def setUp(self):
        self.calcIMC = CalculadoraIMC()  # This will set up the instance for each test

    def test_resultado_magreza(self):
        # Test for IMC category "Magreza"
        self.assertEqual(self.calcIMC.resultado(60, 1.91), "Magreza")
    
    def test_resultado_normal(self):
        # Test for IMC category "normal"
        self.assertEqual(self.calcIMC.resultado(70, 1.75), "normal")
    
    def test_resultado_sobrepeso(self):
        # Test for IMC category "sobrepeso"
        self.assertEqual(self.calcIMC.resultado(85, 1.75), "sobrepeso")
    
    def test_resultado_obesidade(self):
        # Test for IMC category "obesidade"
        self.assertEqual(self.calcIMC.resultado(100, 1.75), "obesidade")

if __name__ == '__main__':
    unittest.main()
