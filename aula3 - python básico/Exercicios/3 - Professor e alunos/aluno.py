
class Aluno:

    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcular_media_notas()
        self.aprovado = self.checar_aprovacao()

    # calcule a média aritmética das 3 notas de cada alunos
    def calcular_media_notas(self):
        m = float(0.0) # media final
        m = (self.nota1 + self.nota2 + self.nota3)/3
        return m

    # imprime se aprovou ou reprovou - nota de aprovação = 7
    def checar_aprovacao(self):
        if self.media >= 7.0:
            return True
        else:
            return False
    