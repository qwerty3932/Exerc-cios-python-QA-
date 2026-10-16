def checar_saldo(saldo):
    print("Saldo atual: ",saldo)

def sacar(saldo):
    x = int(input("Digite a quantidade que deseja sacar: "))
    if x > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= x
    print("Saldo atual: ",saldo)

def depositar(saldo):
    x = int(input("Digite a quantidade que deseja depositar: "))
    saldo += x
    if x < 0:
        print("Valor negativo, cancelando deposito")
        return saldo
    else:
        print("Saldo atual: ",saldo)
        return saldo

def main():
    saldo = int(0)
    while True:
        print("1 - Checar Saldo\n2 - Saque\n3 - Depósito\n4 - Sair")
        x = int(input()) 
        if x == 1:
            checar_saldo(saldo)
        elif x == 2:
            sacar(saldo)
        elif x == 3:
            saldo = depositar(saldo)
        elif x == 4:
            break

main()