# Faça um algoritmo que calcule a multiplicação entre dois números sem utilizar o sinal de multiplicação ( * ) 
# ou função. Utilize estrutura de repetição e soma.

n = int(input("Digite um número: ")) # numero que será multiplicado
m = int(input("Digite outro número: ")) # numero de vezes
r = 0 # resultado
i = 0 # instancia
while i <  m:
    r += n
    i = i + 1
print(r)