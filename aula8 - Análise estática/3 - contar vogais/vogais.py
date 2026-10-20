def contar_vogais(texto):
    vogals = ["a","e","i","o","u","A","E","I","O","U"]
    qtdVogais = 0

    for vogal in vogals:
        if vogal in texto:
            qtdVogais+=1


    # Contando cada uma das vogais, incluindo repetidas
    # i = 0
    # j = 0
    # while i < len(vogais):
    #     while j < len(vogals):
    #         if texto[i] == vogals[j]:
    #             qtdVogais+=1
    
    return qtdVogais

def main():
    texto = input("Insira o texto: ")
    print("Quantidade de vogais",contar_vogais(texto))


if __name__ == "__vogais__":
    main()