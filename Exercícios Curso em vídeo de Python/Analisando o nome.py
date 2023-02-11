'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
  O nome com todoas as letras maíusculas e minúsculas.
  Quanstas letras ao todo (sem considerar espaços).
  Quantas letras tem o primeiro nome.'''

# Zona de teste
# nome_inicial = "Paulo de Souza Marques".


# Declarei uma variável com uma entrada.
nome_inicial = input("Digite seu nome completo: ")
primeiro_nome = nome_inicial.split()

# A saída é através dessse formato de print, eu poderia fazer tudo em um só, mas ficaria muito bagunçado.
print("Seu nome em maiúsculas é {}".format(nome_inicial.upper()))
print("Seu nome em minúsculas é {}".format(nome_inicial.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome_inicial.replace(" ",""))))
print("Seu nome em minúsculas é {}".format(primeiro_nome[0]))




