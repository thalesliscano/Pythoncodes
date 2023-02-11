'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares, Se o valor digitado for ímpar, desconsidere-o'''

#Declarando um acumulador, que vai receber o valor da conta
soma = 0

#Declarando e convertendo dentro de um for para peguntar a quantidade de vezes que desejo repetir
for c in range(1,7):
  numeros_aleatorios = int(input("Digite um número: "))
  if numeros_aleatorios % 2 != 0:
    numeros_aleatorios = 0
  else:
    soma += numeros_aleatorios
print(soma)
