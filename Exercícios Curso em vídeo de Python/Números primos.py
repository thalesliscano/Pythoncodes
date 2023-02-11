'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

# Declarando variáveis
numero = input("Digite um número: ") 

# Convertendo variáveis
numero_convertido = int(numero) 

cores = {
  "limpa":"\033[m",
  "azul":"\033[1,33m"
}

contador = 0
for c in range(1,numero_convertido+1): # 1 2 3 4 5 6 7 8
  if numero_convertido % c == 0 and numero_convertido % 1 == 0: # se NUM(8) % c = 0 e NUM(8) % 1 == 0
    contador += 1
    
if contador > 2:
  print("O número {} foi divisível {} vezes".format(numero,contador))
  print("Não é número primo")
else:
  print("O número {} foi divisível {} vezes".format(numero,contador))
  print("É número primo")
    
  
