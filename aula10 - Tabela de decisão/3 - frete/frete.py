def validar_frete(compra,status_conta):
    return bool(compra >= 150 or status_conta == True)

def main():
    i = input("Assinante? (N - Não, S - Sim):")
    if i == 'N':
        status = False
    elif i == 'S':
        status = True
    
    compra = input("Digite o valor da compra: ")
    print("Valido para frete: ",validar_frete(compra, status))

if __name__ == "__frete__":
    main()