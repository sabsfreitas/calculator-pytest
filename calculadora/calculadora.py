class Calculadora:
    @staticmethod
    def adicionar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b

    @staticmethod
    def potencia(a, b):
        return a ** b

    @staticmethod
    def raiz_quadrada(a):
        if a < 0:
            raise ValueError("Não é possível calcular raiz de número negativo.")
        return a ** 0.5
