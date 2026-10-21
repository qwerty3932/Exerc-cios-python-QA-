def validar_idade_desconto(idade):
    desconto = False
    if idade >= 0 and idade <= 17:
        desconto = True
    elif idade >= 18 and idade <= 59:
        desconto = False
    elif idade >= 60 and idade <= 120:
        desconto = True
    else:
        raise ValueError("Valor inválido")

    return desconto

def main():
    idade = int(input("Idade: "))
    print("Valido para desconto: ",validar_idade_desconto(idade))


