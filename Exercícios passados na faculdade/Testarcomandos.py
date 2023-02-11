'''Esse programa identifica quantos números positivo e soma eles posteriormente'''

# Declarando variáveis e convertendo para inteiro
numero_1,numero_2,numero_3,numero_4 = map(int,input().split())

# Varias condições que vai contando e  somando os positivos, e caso seja >, caso seja <= 0, vai diminuindo um na soma 
# Caso todos sejam positivos (+ + + +)
if numero_1 > 0 and numero_2 > 0 and numero_3 > 0 and numero_4 > 0:
   soma = numero_1 + numero_2 + numero_3 + numero_4
   aux = 4
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

# Caso o primeiro seja negativo (- + + +)
elif numero_1 <= 0 and numero_2 > 0 and numero_3 > 0 and numero_4 > 0:
   soma = numero_2 + numero_3 + numero_4
   aux = 3
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

# Caso o primeiro e segundo seja negativo (- - + +)
elif numero_1 <= 0 and numero_2 <= 0 and numero_3 > 0 and numero_4 > 0:
   soma = numero_3 + numero_4
   aux = 2
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

# Caso o terceiro e quarto seja negativo(+ + - -)
elif numero_1 > 0 and numero_2 > 0 and numero_3 <= 0 and numero_4 <= 0:
   soma = numero_1 + numero_2
   aux = 2
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))
# Caso o primeiro e terceiro seja negativo (- + - +)
elif numero_1 <= 0 and numero_2 > 0 and numero_3 <= 0 and numero_4 > 0:
   soma = numero_2 + numero_4
   aux = 2
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))
# Caso o segundo e quarto seja negativo (+ - + -)
elif numero_1 > 0 and numero_2 <= 0 and numero_3 > 0 and numero_4 <= 0:
   soma = numero_1 + numero_3
   aux = 2
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

# Caso o primeiro,segundo e terceiro seja negativo(- - - +) 
elif numero_1 <= 0 and numero_2 <= 0 and numero_3 <= 0 and numero_4 > 0:
   soma = numero_4
   aux = 1
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

# caso o primeiro, segundo, terceiro e quarto seja negativo (- - - -)
elif numero_1 <= 0 and numero_2 <= 0 and numero_3 <= 0 and numero_4 <= 0:
   soma = 0
   aux = 0
   print('Número de positivos lidos: {0:d}'.format(aux))
   print('Soma dos números positivos: {0:d}'.format(soma))

 

