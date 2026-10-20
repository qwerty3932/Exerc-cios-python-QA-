from vogais import contar_vogais


def teste_maiusculo():
    texto = "TESTE"
    assert contar_vogais(texto) == 1

def teste_minusculo():
    texto = "teste teste abc"
    assert contar_vogais(texto) == 2

def teste_sem_vogais():
    texto = "cccc"
    assert contar_vogais(texto) == 0

def teste_vazio():
    texto = ""
    assert contar_vogais(texto) == 0