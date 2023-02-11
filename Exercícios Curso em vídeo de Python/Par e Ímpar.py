'''Crie um programa que leia um número inteiro e mostre na tela se ela é PAR ou ÍMPAR.'''

# Declarando variável
num_incial = input()

# Convertendo variável
num_convertido = int(num_incial)

# Condicionai pra saber se o número é PAR ou ÍMPAR
if num_convertido % 2  == 0:
  print("Esse número é PAR")
else:
  print("Esse número é ímpar")
