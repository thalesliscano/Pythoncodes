# Treino de for 
'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
cont = 0
soma = 0 

for i in range(1,501,2):
  if i % 3 == 0:
    soma += i
    cont += 1
print("De todos os {} números, a soma de todos os números ímpares é {}".format(cont,soma))
    