from login import logar


def teste_senha_conta():
    assert logar("senha", False) == True

def teste_senha_conta_bloqueada():
    assert logar("senha", True) == False

def teste_senha_errada():
    assert logar("ssenha", False) == False

def teste_senha_errada_conta_bloqueada():
    assert logar("ssenha", True) == False