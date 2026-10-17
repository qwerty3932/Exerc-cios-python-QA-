class Produto:
    def __init__(self, nome, marca, data_fabricacao, disponivel, preco):
        self.nome = nome
        self.marca = marca
        self.data_fabricacao = data_fabricacao
        self.disponivel = disponivel 
        self.preco = preco

    def cadastrar_produto(self):
        nome = input("Nome: ")
        marca = input("Marca: ")
        data_fabricacao = input("Data de fabricação: ")
        disponivel = bool(input("Disponibilidade do produto (0 - indisponivel, 1 - disponivel): "))
        preco = float(input("Preço: "))
        novo_produto = Produto(nome, marca, data_fabricacao, disponivel, preco)
        return novo_produto