maior = 0
menor = 0
i = 0
x = 5
while i < x:
    num = int(input())
    if i == 0:
        maior = num
        menor = num
        i +=1
        continue

    if num > maior:
        maior = num
    elif num < maior and num < menor:
        menor = num
    i +=1

print(f"Número maior: {maior}\nNúmero menor: {menor}")
