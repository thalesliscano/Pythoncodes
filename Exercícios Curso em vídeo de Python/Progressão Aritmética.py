'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa pregressão.'''

# Declarando variáveis e convertendo variáveis
from ast import If

# Declarando variáveis de entrada e as convertendo 
primeiro_termo = int(input("Primeiro termo: "))
razao_da_progressao = int(input("Razão: "))

# Conta para se chegar no numero limite do laço for
ultimo = primeiro_termo + 10 * razao_da_progressao

print("=" * 15)
print("10 TERMOS DE UM PA")
print("=" * 15)

for i in range(primeiro_termo,ultimo,razao_da_progressao):
  print(" {} ".format(i),end="➞ ")
print("Acabou")

  