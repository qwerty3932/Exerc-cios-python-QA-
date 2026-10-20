def calcular_total(precos,desconto):
    i = 0
    soma = 0
    while i < len(precos):
        soma+=precos[i]
        i+=1
    desconto = (desconto/100) * soma
    total_preco = soma - desconto
    return total_preco

def definir_desconto():
    try:
        desconto = int(input("Percentual de desconto total: "))
    except ValueError:
        raise ValueError("Valor inválido")
    if desconto < 0 or desconto > 100:
        raise ValueError("Valor inválido")
    return desconto

def definir_itens(quantidade):
    precos = []
    i = 0
    while i < quantidade:
            print("Digite o valor do próximo item: ")
            novo_preco = float(input())
            if novo_preco <= 0:
                print("Valor inválido")
                continue
            else:
                i+=1
                precos.append(novo_preco)
                print("Valor adicionado a lista.")
    return precos

def main():
    precos = []
    d = definir_desconto()
    q = int(input("Quantos itens entrarão na lista: "))

    precos = definir_itens(q)
    
    print("Preço total (após desconto): ",calcular_total(precos,d))
    
if __name__ == "__loja__":    
    main()