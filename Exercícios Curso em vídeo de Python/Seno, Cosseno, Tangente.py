from cmath import cos, tan
from math import radians, sin
'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
# ZOna de teste
# valor_angulo_inicial = "45"

# Declarando variável 
valor_angulo_inicial = input()

#Convertendo variável
valor_angulo_convertido = int(valor_angulo_inicial)

# Resolvendo problema
seno = sin(radians(valor_angulo_convertido))
cosseno = cos(radians(valor_angulo_convertido))
tangente = tan(radians(valor_angulo_convertido))

# Imprimindo o resultado de acordo com o valor desejado. 
print("o valor do ângulo para: ")
print("SENO é: {:.2f}".format(seno))
print("COSSENO é: {:.2f}".format(cosseno))
print("TANGENTE é: {:.2f}".format(tangente))



