def multi(a,b):
    r = 0 # a soma final
    i = 0
    while i < b:
        r += a
        i = i + 1
    return r

def main():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite a quantidade de vezes que será repetido: "))
    print(multi(x,y))

main()