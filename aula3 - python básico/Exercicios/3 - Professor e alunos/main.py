# Escreva um algoritmo que o professor informa quantos alunos possui
# O professor deve informar 3 notas de cada aluno (?) 
# calcule a média aritmética das 3 notas de cada alunos 
# imprime se aprovou ou reprovou - nota de aprovação = 7
# apresenta média de cada aluno
# apresente a média da turma inteira
# a porcentagem de alunos aprovados e reprovados.
from aluno import Aluno
from turma import Turma


def main():
    turma1 = Turma()

    # Objetos criados para teste
    # novo_aluno1 = Aluno("joao", 7, 7, 7)
    # novo_aluno2 = Aluno("maria", 8, 8, 8)
    # novo_aluno3 = Aluno("pedro", 9, 9, 9)
    # turma1.registrar_aluno(novo_aluno1)
    # turma1.registrar_aluno(novo_aluno2)
    # turma1.registrar_aluno(novo_aluno3)
    
    
    while True:
        print("1 - Adicionar aluno e notas\n2 - Listar alunos\n3 - Média da turma" \
        "\n4 - Porcentagem de aprovados e reprovados\n5 - sair")
        x = int(input()) 
        if x == 1:
            Aluno.novo_aluno(turma1)
        elif x == 2:
            Turma.listar_turma(turma1)
        elif x == 3:
            Turma.calcular_media_turma(turma1)
        elif x == 4:
            Turma.calcular_porcentagem_turma_aprovados(turma1)   
        elif x == 5:
            break

main()