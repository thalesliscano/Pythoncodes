'''O mesmo professor do desafio anterior quer sortear a apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''


from random import shuffle

# Zona de teste
# aluno_um = "thales"
# aluno_dois = "vinicius"
# aluno_tres = "sergio"
# aluno_quatro = "naura"

# Declarando Variáveis
aluno_um = input()
aluno_dois = input()
aluno_tres = input()
aluno_quatro = input()


# Sorteando variáveis
lista_nomes = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
shuffle(lista_nomes)

# Imprimindo o resultado de acordo com a saída desejada.
# print("A ordem de apresentação é:  {}".format(shuffle(sorteio)))
print("A ordem de apresentação é:  {}".format(lista_nomes))

