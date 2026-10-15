def main():
    b = int(input("Base: "))
    e = int(input("Expoente: "))

    r = b # resultado

    i = 0
    while i < e:
        if i == 0:
            print(r)
            i+=1
            continue
        r = r*b
        print(r)
        i+=1
        
main()