from secrets import choice
'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

#TESTE
# aluno_um = "thales"
# aluno_dois = "vinicius"
# aluno_tres = "sergio"
# aluno_quatro = "naura"

# Declrando variáveis

aluno_um = input()
aluno_dois = input()
aluno_tres = input()
aluno_quatro = input()

# Sorteando
sorteio = aluno_um, aluno_dois, aluno_tres, aluno_quatro 

# Imprimindo o resultado de acordo com a saída desejada.
print("O aluno escolhido foi {}".format(choice(sorteio)))


