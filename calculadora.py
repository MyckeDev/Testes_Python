class Calculadora:
    # Método de soma
    def soma(self, n1, n2):
        return n1 + n2

    # Método de subtração
    def subtracao(self, n1, n2):
        return n1 - n2

    # Método de multiplicação
    def multiplicacao(self, n1, n2):
        return n1 * n2

    # Método de divisão com verificação de divisão por zero
    def divisao(self, n1, n2):
        if n2 == 0:
            return "Erro: Divisão por zero não é permitida."
        else:
            return n1 / n2
    