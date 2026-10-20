
class Aluno:

    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcular_media_notas()
        self.aprovado = self.checar_aprovacao()

    def novo_aluno(turma):
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        novo_aluno = Aluno(nome, nota1, nota2, nota3)
        turma.registrar_aluno(novo_aluno)

    # calcule a média aritmética das 3 notas de cada alunos
    def calcular_media_notas(self):
        m = 0.0 # media final
        m = (self.nota1 + self.nota2 + self.nota3)/3
        return m

    # imprime se aprovou ou reprovou - nota de aprovação = 7
    def checar_aprovacao(self):
        return self.media >= 7.0