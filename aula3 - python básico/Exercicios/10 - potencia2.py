def main():
    b = int(input("Base: "))
    e = int(input("Expoente: "))

    r = b # resultado

    i = 0
    j = 0
    while i < e:
        if i == 0:
            print(r)
            i+=1
            continue
        # r = r*b
        while j < r:
            r += r
            j += 1
    
        print(r)
        i+=1
        
main()