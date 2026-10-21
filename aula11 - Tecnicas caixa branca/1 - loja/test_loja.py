from loja import definir_desconto


def teste_vip_compra_acima():
    assert definir_desconto(201, True) == True

def teste_vip_compra_abaixo():
    assert definir_desconto(199, True) == False

def teste_compra_acima():
    assert definir_desconto(201, False) == False

def teste_compra_abaixo():
    assert definir_desconto(199, False) == False