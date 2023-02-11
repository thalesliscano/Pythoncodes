#Dando uma medida de tempo em segundos, esse programa em python computa o número de horas,minutos e segundos
#Entrada do tipo inteiro

#Zona de teste
# numInteiroEmSegundos = int("3600")

#Entrada
numInteiroEmSegundos = int(input())

#Calculando horas 
hora = numInteiroEmSegundos // 3600
#Calculando minutos 
minutos = numInteiroEmSegundos // 60 % 60
# aux = minutos % 60
#Calculando segundos 
segundos = numInteiroEmSegundos % 60

#Imprimindo os valores conseguidos para mostrar quantas horas, minutos e segundos representa o valor em segundos.
print("{} {} {}".format(hora,minutos,segundos))

#depurando
# print(aux)