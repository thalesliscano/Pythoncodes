'''Faça um programa que leia um núemro inteiro e diga se ele é ou não um número primo.'''

# Declarando variáveis
numero = input("Digite um número: ")

# Convertendo variáveis
numero_convertido = int(numero)


contador = 0
for c in range(1,numero_convertido+1):
  print("{}".format(c), end= " ")
if c % 1 == 0 and c % c == 0:
  contador += 1
  print("O número {} foi divisível {} vezes".format(numero,contador))
    
    
  print("dios")
print("O número foi{".format(contador))

print(".")