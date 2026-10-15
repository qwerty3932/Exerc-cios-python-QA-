def main():
    print("Os números devem ser maior que 0 e inteiros")
    while True:
        x = int(input("Digite o primeiro número: "))
        if x <= 0:
            print("Valor inválido")
            continue
        y = int(input("Digite a quantidade de vezes que será repetido: "))
        if y <= 0:
            print("Valor inválido")
            continue
        break

    r = 0 # a soma final
    i = 0
    while i < y:
        r += x
        i = i + 1
    return r

main()