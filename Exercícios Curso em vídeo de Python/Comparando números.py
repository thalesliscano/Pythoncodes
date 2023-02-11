'''Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro é maior 
- O segundo é menor
- Não existe valor maior, os dois são iguais 
'''

# Declarando variáveis 
numero_um = input("Digite um número inteiro: ")
numero_dois = input("Digite um número inteiro: ")

# Convertendo variáveis 
primeiro_numero_convertido = int(numero_um)
segundo_numero_convertido = int(numero_dois)

# Condicionais, vai ver se qual número é maior e imprimir na tela, caso os números sejam iguais, era imprimir que ambos são iguais.
if primeiro_numero_convertido > segundo_numero_convertido:
  print("O primeiro número é maior")
elif segundo_numero_convertido > primeiro_numero_convertido:
  print("O segundo número é maior")
elif primeiro_numero_convertido == segundo_numero_convertido:
  print("Não existe número maior, ambos são iguais")


