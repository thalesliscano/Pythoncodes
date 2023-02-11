'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep


contagem_limite = 10
for i in range(10,-1,-1):
  sleep(0.5)
  print(i)
print("BUM!  BUM!! POOW!!")

