def definir_desconto(total,vip):
    if vip == True and total >= 200:
        return True
    else:
        return False

def main():
    preco_total = 0
    i = input("Cliente Vip? (N - Não, S - Sim):")
    if i == 'N':
        cliente_vip = False
    elif i == 'S':
        cliente_vip = True

    desconto = definir_desconto(preco_total,cliente_vip)
    print("Valido para desconto: ",desconto)



if __name__ == "__loja__":
    main()