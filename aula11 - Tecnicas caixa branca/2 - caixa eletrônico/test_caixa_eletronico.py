import caixa_eletronico 

def teste_deposito_e_checagem():
    novo_saldo = caixa_eletronico.depositar(10,20)
    assert caixa_eletronico.checar_saldo(novo_saldo) == 30

def teste_deposito_negativo():
    assert caixa_eletronico.depositar(-10,20) == 20 # O deposito é ignorado

def teste_sacar():
    assert caixa_eletronico.sacar(20, 30) == 10

def teste_sacar_negativo():
    assert caixa_eletronico.sacar(20, 10) == False
    