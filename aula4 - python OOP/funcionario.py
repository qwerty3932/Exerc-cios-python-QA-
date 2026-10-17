from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, endereco, telefone, email, salario, posicao):
        super().__init__(nome, sobrenome, endereco, telefone, email)
        self.salario = salario
        self.posicao = posicao
    
    def cadastrar(self):
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        salario = input("Salário: ")
        posicao = input("Posição:")
        novo_funcionario = Funcionario(nome, sobrenome, endereco, telefone, email, salario, posicao)
        return novo_funcionario
        
    