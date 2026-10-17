from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, endereco, telefone, email):
        super().__init__(nome, sobrenome, endereco, telefone, email)
    
    def cadastrar(self):
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        novo_cliente = Cliente(nome, sobrenome, endereco, telefone, email)
        return novo_cliente
        
    