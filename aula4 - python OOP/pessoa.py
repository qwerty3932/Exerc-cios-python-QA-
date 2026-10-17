
class Pessoa:
    def __init__(self, nome, sobrenome, endereco, telefone, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def cadastrar(self):
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        nova_pessoa = Pessoa(nome, sobrenome, endereco, telefone, email)
        return nova_pessoa


    