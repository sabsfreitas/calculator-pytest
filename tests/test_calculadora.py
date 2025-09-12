import pytest
from calculadora.calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_adicionar(calc):
    assert calc.adicionar(2, 3) == 5

def test_subtrair(calc):
    assert calc.subtrair(10, 4) == 6

def test_multiplicar(calc):
    assert calc.multiplicar(3, 5) == 15

def test_dividir(calc):
    assert calc.dividir(10, 2) == 5

def test_dividir_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(5, 0)

def test_potencia(calc):
    assert calc.potencia(2, 4) == 16

def test_raiz_quadrada(calc):
    assert calc.raiz_quadrada(25) == 5

def test_raiz_quadrada_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-9)
