import pytest
from calculadora.calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.operacoes_basicas
@pytest.mark.smoke
@pytest.mark.parametrize(
    "metodo, a, b, esperado",
    [
        ("adicionar", 2, 3, 5),
        ("subtrair", 10, 4, 6),
        ("multiplicar", 3, 5, 15),
        ("dividir", 10, 2, 5),
    ]
)
def test_operacoes_basicas(calc, metodo, a, b, esperado):
    assert getattr(calc, metodo)(a, b) == esperado

@pytest.mark.extras
def test_potencia(calc):
    assert calc.potencia(2, 4) == 16

@pytest.mark.extras
def test_raiz_quadrada(calc):
    assert calc.raiz_quadrada(25) == 5

@pytest.mark.excecoes
def test_dividir_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(5, 0)

@pytest.mark.excecoes
def test_raiz_quadrada_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-9)
