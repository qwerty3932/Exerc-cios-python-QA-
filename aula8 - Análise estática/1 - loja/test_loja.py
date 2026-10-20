import loja
import pytest


def teste_varios_precos_sem_desconto(monkeypatch):
    input = iter([5,10,15,20,25])
    monkeypatch.setattr('builtins.input', lambda *args: next(input))

    q = 5
    d = 0
    precos = loja.definir_itens(q)
    total_preco = loja.calcular_total(precos,d)
    assert total_preco == 75


def teste_compra_desconto(monkeypatch):
    input = iter([5,10,15,20,25])
    monkeypatch.setattr('builtins.input', lambda *args: next(input))

    q = 5
    d = 10
    precos = loja.definir_itens(q)
    total_preco = loja.calcular_total(precos,d)
    assert total_preco == 67.5

def teste_lista_vazia():
    q = 0
    d = 0
    precos = loja.definir_itens(q)
    assert loja.calcular_total(precos,d) == 0
    

def teste_desconto_abaixo(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: -1)
    with pytest.raises(ValueError):
        loja.definir_desconto()

def teste_desconto_acima(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 101)
    with pytest.raises(ValueError):
        loja.definir_desconto()

