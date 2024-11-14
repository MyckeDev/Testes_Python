class CalculadoraIMC:
    def resultado(self, peso, altura):
        imc = peso / (altura * altura)
        
        # Checking the IMC range and returning the corresponding category
        if imc < 19:
            return "Magreza"
        elif 19 <= imc < 24:
            return "normal"
        elif 24 <= imc < 29:
            return "sobrepeso"
        else:
            return "obesidade"
