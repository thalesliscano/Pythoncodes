#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#Declarando váriavel
numero_da_tabuada = int(input())

for i in range(1,11):
  print("{} X {} = {}".format(numero_da_tabuada, i, numero_da_tabuada * i))
print("")
