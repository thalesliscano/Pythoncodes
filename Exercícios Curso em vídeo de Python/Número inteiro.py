from math import floor, trunc 
'''Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua poção inteira.'''

# Nesse exercício comei a usar mais a biblioteca do python
#Declarar variável
primeiro_numero = input()


# Converter variável
primeiro_numero = float(primeiro_numero)


# Imprimindo resutlado de acordo com a saída desejada
print("{}".format(trunc(primeiro_numero)))