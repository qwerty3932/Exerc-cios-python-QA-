# Classe de equivalência - Valores - Resultado esperado
# idade menor que 18 | 0 a 17 | Valido
# idade entre 18 e 59 | 18 a 59 | Invalido
# idade maior que 60 | 61 a 120 | Valido
# Valor que não é uma idade valida | Texto, número negativo ou acima de 120 | Invalido (ValueError)
# 
# -1 - ValueError
# 0 - Desconto para crianças/adolescentes
# 17 - Desconto para crianças/adolescentes
# 18 - Valor integral 
# 59 - Valor integral 
# 60 - Desconto para idosos 
# 120 - Desconto para idosos
# 121 - ValueError
import pytest
from idade import validar_idade_desconto


def teste_idade_abaixo():
    with pytest.raises(ValueError):
        validar_idade_desconto(-1)

def teste_idade_menor():
    assert validar_idade_desconto(0) == True

def teste_idade_adulto():
    assert validar_idade_desconto(18) == False

def teste_idade_adulto_velho():
    assert validar_idade_desconto(59) == False

def teste_idade_velho():
    assert validar_idade_desconto(60) == True

def teste_idade_muito_velho():
    assert validar_idade_desconto(120) == True

def teste_idade_acima():
    with pytest.raises(ValueError):
        validar_idade_desconto(121)