def main():
    primos = []
    primos_maior_que_1000 = 0

    soma = 0
    maior = 0
    menor = 0
    i = 0

    x = int(input("Quantidade de números: "))

    while i < x:
        novo_valor = int(input())
        if novo_valor <= 0:
            print("Digite números maiores que 0")
            continue
        else:
            if novo_valor%2 == 0:
                if i == 0:
                    maior = novo_valor
                    menor = novo_valor
                else:
                    if novo_valor > maior:
                        maior = novo_valor
                    elif novo_valor < maior and novo_valor < menor:
                        menor = novo_valor
                    if novo_valor > 1000:
                        primos_maior_que_1000+=1
                    print("Número primo.")
                    primos.append(novo_valor)
                    soma+=novo_valor
                    i+=1
            else:
                print("Número não primo.")
                i+=1
    media_final = soma/len(primos)
    print(f"Quantidade de números primos e maiores que 1000: {primos_maior_que_1000} \
          \nMaior número: {maior}\nMenor número: {menor}\nMédia aritmética: {media_final}")

    
main()