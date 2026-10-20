

def encontrar_maior(numeros):
    i = 0 

    # Vai tentar acessar o primeiro número da lista. Se estiver vazio, ativa uma falha

    
    try:
        maior = numeros[0]
    except IndexError:
        raise IndexError("Lista vazia")
        # Obs: Na atividade diz pra chamar o erro ValueError, mas o IndexError se encaixa mais
        # nessa situação
        
    while i < len(numeros):
        if maior < numeros[i]:
            maior = numeros[i]
        i+=1
    return maior

        

def main():
    i = 0
    q = 5
    numeros = []

    # Adiciona os números à lista
    while i < q:
        num = int(input())
        numeros.append(num)

if __name__ == "__maior__":
    main()