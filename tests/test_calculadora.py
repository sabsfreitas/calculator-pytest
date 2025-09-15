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
        # Casos básicos
        ("adicionar", 2, 3, 5),
        ("subtrair", 10, 4, 6),
        ("multiplicar", 3, 5, 15),
        ("dividir", 10, 2, 5),

        # Casos com números negativos
        ("adicionar", -1, -1, -2),
        ("subtrair", -5, -2, -3),
        ("multiplicar", -3, 5, -15),
        ("multiplicar", -3, -3, 9),
        
        # Casos envolvendo zero
        ("adicionar", 10, 0, 10),
        ("subtrair", 0, 5, -5),
        ("multiplicar", 100, 0, 0),
        ("dividir", 0, 5, 0),

        # Casos com ponto flutuante (float)
        ("adicionar", 2.5, 2.5, 5.0),
        ("dividir", 5.0, 2, 2.5),
    ]
)
def test_operacoes_basicas(calc, metodo, a, b, esperado):
    assert getattr(calc, metodo)(a, b) == esperado

@pytest.mark.extras
@pytest.mark.parametrize(
    "base, expoente, esperado",
    [
        (2, 4, 16),
        (10, 0, 1),      # Qualquer número elevado a 0 é 1
        (5, 1, 5),       # Qualquer número elevado a 1 é ele mesmo
        (0, 5, 0),       # Zero elevado a qualquer potência (positiva) é 0
        (-3, 2, 9),      # Base negativa com expoente par
        (-3, 3, -27),    # Base negativa com expoente ímpar
    ]
)
def test_potencia(calc, base, expoente, esperado):
    assert calc.potencia(base, expoente) == esperado

@pytest.mark.extras
@pytest.mark.parametrize(
    "numero, esperado",
    [
        (25, 5),
        (0, 0),          # Raiz quadrada de 0
        (1, 1),          # Raiz quadrada de 1
        (144, 12),       # Quadrado perfeito
    ]
)
def test_raiz_quadrada(calc, numero, esperado):
    """Testa a raiz quadrada de quadrados perfeitos."""
    assert calc.raiz_quadrada(numero) == esperado

@pytest.mark.extras
def test_raiz_quadrada_precisao(calc):
    """
    Testa a raiz de um número não perfeito,
    verificando a precisão do ponto flutuante.
    """
    assert calc.raiz_quadrada(2) == pytest.approx(1.41421356)

# --- Testes de exceções ---

@pytest.mark.excecoes
def test_dividir_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(5, 0)

@pytest.mark.excecoes
def test_raiz_quadrada_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-9)

@pytest.mark.excecoes
def test_potencia_zero_elevado_negativo(calc):
    with pytest.raises(ZeroDivisionError):
        calc.potencia(0, -1) # 1/0

@pytest.mark.excecoes
@pytest.mark.parametrize(
    "metodo, a, b",
    [
        ("adicionar", "a", 5),
        ("subtrair", 10, "b"),
        ("multiplicar", 3, {1, 2, 3}),
        ("dividir", 10, {"a": 1}),
    ]
)
def test_entrada_invalida_type_error(calc, metodo, a, b):
    with pytest.raises(TypeError):
        getattr(calc, metodo)(a, b)