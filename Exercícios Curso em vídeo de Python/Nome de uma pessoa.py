'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA no nome."'''

#Zona de teste
nome_incial = "Thales Liscano"

# Declrando 
# nome_incial = input()

#Resolvendo problemas  
ajustando_fonte = nome_incial.casefold()
encontre_nome = "silva" in ajustando_fonte  

# Imprimindo o resultado de acordo com a saída desejada.
print(encontre_nome)