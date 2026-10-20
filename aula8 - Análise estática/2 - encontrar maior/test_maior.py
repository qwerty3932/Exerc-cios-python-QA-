import pytest
from maior import encontrar_maior


def teste_lista_positiva():
    test_numeros = [1,2,3,4,5]

    assert encontrar_maior(test_numeros) == 5

def teste_lista_negativa():
    test_numeros = [-1,-2,-3,-4,-5]

    assert encontrar_maior(test_numeros) == -1

def teste_lista_repetida():
    test_numeros = [1,1,1,1,1]

    assert encontrar_maior(test_numeros) == 1

def teste_lista_vazia():
    test_numeros = []
    
    with pytest.raises(IndexError):
        encontrar_maior(test_numeros)

def teste_lista_positivo_negativo():
    test_numeros = [5,-1,-2,-3,-4]

    assert encontrar_maior(test_numeros) == 5