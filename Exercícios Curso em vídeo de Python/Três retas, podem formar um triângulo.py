'''Desenvolva um programa que leia o comprimento de três retas e diga ao usário se elas podem ou não formar um triângulo.'''

# Zona de teste
from ast import Num


# primeiro_comprimento = "2" 
# segundo_comprimento =  "4"
# terceiro_comprimento = "9"


# Declarando variáveis 
primeiro_comprimento = input("Primeiro segmento: ") 
segundo_comprimento = input("Segundo segmento:")
terceiro_comprimento = input("Terceiro segmento: ")

# Converendo variáveis 
primeiro_comprimento_convertido = float(primeiro_comprimento)
segundo_comprimento_convertido = float(segundo_comprimento)
terceiro_comprimento_convertido = float(terceiro_comprimento)

#Lendo três comprimentos de três retas aonde vamos ver se as mesmas formam um triângulo. 
#Se a soma entre os lados é igual o terceiro esse triãngulo pode existir.
#Basta somar os dois lados menores, sendo soma entre eles maiores que o terceiro lado, então, a sema entre qualquer um deles e o terceiro é maior

# Então se 1º for menor que o 3º ele vai ser somado. Se o 2º for menor que o 3º ele vai ser somado com o um
somar_comprimentos = primeiro_comprimento_convertido + segundo_comprimento_convertido 
print("=-=" * 40)
print("Analisador de Triângulos")
print("=-=" * 40)

if somar_comprimentos > terceiro_comprimento_convertido:
  print("Os segmentos acima PODEM formar um triângulo.")
else:
  print("Os segmentos acima NÃO PODEM formar um triângulo.")
print("=-=" * 40)


  