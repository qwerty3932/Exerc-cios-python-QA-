from frete import validar_frete

def teste_compra_acima_assinante():
    assert validar_frete(151, True) == True

def teste_senha_conta_bloqueada():
    assert validar_frete(151, False) == True

def teste_senha_errada():
    assert validar_frete(1, True) == True

def teste_senha_errada_conta_bloqueada():
    assert validar_frete(1, True) == False