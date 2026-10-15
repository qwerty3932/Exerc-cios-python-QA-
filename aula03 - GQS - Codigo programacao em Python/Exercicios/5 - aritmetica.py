def main():
    aritmetica = []
    n = int(input("Número de termos: "))
    a1 = int(input("Primeiro termo: "))
    r = int(input("Razão: "))
    novo_valor = 0
    i = 0
    while i < n:
        if i == 0:
            aritmetica.append(a1)
        else:
            novo_valor = aritmetica[i-1]+r
            aritmetica.append(novo_valor)
        i+=1

    for num in aritmetica:
        print(num)

main()



