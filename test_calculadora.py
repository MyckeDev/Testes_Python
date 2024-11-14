# Importar a classe "Calculadora"
from calculadora import Calculadora
import unittest

class TestCalculadora(unittest.TestCase):
    
    # Configurar o ambiente de testes
    def setUp(self):
        self.calc = Calculadora()

    # Criar o teste para o método soma
    def test_soma(self):
        self.assertEqual(self.calc.soma(20, 30), 50, "Deve somar dois números")
        self.assertEqual(self.calc.soma(200, 300), 500, "Deve somar dois números")

    # Criar o teste para o método subtração
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(10, 2), 8, "Deve subtrair dois números")
        self.assertEqual(self.calc.subtracao(10, 30), -20, "Deve resultar em um valor negativo")

    # Criar o teste para o método multiplicação
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(5, 4), 20, "Deve multiplicar dois números")

    # Criar o teste para o método divisão
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10, 2), 5, "Deve dividir dois números")

    # Criar método de teste para divisão por 0
    def test_divisao_por_zero(self):
        self.assertEqual(self.calc.divisao(1, 0), "Erro: Divisão por zero não é permitida.")

if __name__ == '__main__':
    unittest.main()

