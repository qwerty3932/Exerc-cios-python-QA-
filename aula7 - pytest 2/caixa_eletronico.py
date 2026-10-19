def checar_saldo(saldo):
    print("Saldo atual: ",saldo)
    return saldo

def sacar(input, saldo):
    if input > saldo:
        print("Saldo insuficiente")
        return False
    else:
        saldo -= input
        print("Saldo atual: ",saldo)
        return saldo
    

def depositar(input, saldo):
    if input < 0:
        print("Valor negativo, cancelando deposito")
        return saldo
    else:
        saldo += input
        print("Saldo atual: ",saldo)
        return saldo

def main():
    saldo = float(0)
    x = 0
    while True:
        print("1 - Checar Saldo\n2 - Saque\n3 - Depósito\n4 - Sair")
        x = int(input()) 
        if x == 1:
            checar_saldo(saldo)
        elif x == 2:
            input = float(input("Digite a quantidade que deseja sacar: "))
            if sacar(input, saldo) != False:
                saldo = sacar(input, saldo)
        elif x == 3:
            input = float(input("Digite a quantidade que deseja depositar: "))
            saldo = depositar(input, saldo)
        elif x == 4:
            break

if __name__ == "__main__":
    main()