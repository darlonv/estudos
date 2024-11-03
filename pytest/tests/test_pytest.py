import sys
from pytest import mark
from codigo.jogo import brincadeira

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1
    esperado = 1
    resultado = brincadeira(entrada)
    assert resultado == esperado

def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    entrada = 2
    esperado = 2
    resultado = brincadeira(entrada)
    assert resultado == esperado

def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == "queijo"

@mark.goiabada
@mark.smoke
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == "goiabada"

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(5) == "goiabada"

@mark.goiabada
def test_quando_brincadeira_receber_20_entao_deve_retornar_goiabada():
    assert brincadeira(5) == "goiabada"

@mark.skip(reason="Não implementado")
def test_quando_brincadeira_receber_negativo_entao_deve_retornar_0():
    assert brincadeira(-1) == "goiabada"


@mark.parametrize(
        'entrada',
        [5, 10, 20, 25, 25]
        )
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == "goiabada"

@mark.parametrize(
        'entrada',
        [3, 6, 9, 12, 18]
        )
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada):
    assert brincadeira(entrada) == "queijo"


@mark.parametrize(
        'entrada, esperado',
        [(1,1),
         (2,2),
         (3,"queijo"),
         (4,4),
         (5,"goiabada"),
         (6,"queijo"),
         (7,7),
         (8,8),
         (9,"queijo"),
         (10,"goiabada"),
         (11,11),
         (12,"queijo"),
         (13,13),
         (14,14),
         (15,"romeu e julieta")
         ]
        )
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada, esperado):
    assert brincadeira(entrada) == esperado