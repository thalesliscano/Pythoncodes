'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" '''
import math 
# zona de teste 
# nome_cidade_inicial = "santos gunari".split()

# Declarando variável
nome_cidade_inicial = input().split()

# Aqui eu pego apenas o indice 0, sendo se for "SANTOS" irá ter como resutlado "True" e "False" não tendo. 
apenasSantos = nome_cidade_inicial[0]
aux = apenasSantos.casefold()
semEspaço = aux.strip()
aux2 = "santo" in semEspaço

# Imprimindo o resultado de acordo com a saída desejada.
print(aux2)

# print("{}".format(aux))