def main():

    while True:
        print("Digite 0 para encerrar programa")
        novo_valor = int(input())
        if novo_valor == 0:
            break
        else:
            if novo_valor%2 == 0:
                print("Número primo.")
            else:
                print("Número não primo.")
    
main()

