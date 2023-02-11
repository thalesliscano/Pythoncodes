'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usário tentar descobrir qual foi o número escolhido pelo computador. O programa devera escrever na tela se o usuário perdeu ou venceu.'''

# Declarando 
from random import randint, random


usuario_adivinha = input()
numero_aleatorio = randint(0,5)
# Convertendo variável
usuario_adivinha_convertido = int(usuario_adivinha)

# Imprimindo o resultado de acordo a saída desejada. 
print(usuario_adivinha_convertido)
print(numero_aleatorio)

