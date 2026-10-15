
class Turma:
    
    def __init__(self):
        self.turma = []

    def registrar_aluno(self, aluno):
        self.turma.append(aluno)
        print(f"{aluno.nome} registrado como aluno na turma com sucesso.")

    # apresenta média de cada aluno
    def listar_turma(self):
        if len(self.turma) == 0:
            print("Não há alunos na turma")
        else:
            print("Alunos na turma")
            for aluno in self.turma:
                print(f"{aluno.nome} - Nota média: {aluno.media}")


    # a porcentagem de turma aprovados e reprovados.
    def calcular_porcentagem_turma_aprovados(self):
        aprovados = 0

        if len(self.turma) == 0:
            print("Não há alunos na turma")
        else:
            for aluno in self.turma:
                if aluno.aprovado == True:
                    aprovados+=1
            porcentagem_aprovados = (aprovados/len(self.turma))*100
            print(porcentagem_aprovados)
            


    # apresente a média da turma inteira
    def calcular_media_turma(self):
        if len(self.turma) == 0:
            print("Não há alunos na turma")
        else:
            media_total = 0
            for aluno in self.turma:
                media_total += aluno.calcular_media_notas()
            media_total = media_total/len(self.turma)
            print(f"Média da turma = {media_total}")
