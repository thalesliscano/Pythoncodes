from math import ceil, sqrt,floor

'''faça um programa que leia o comprimento do cateto oposto a do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

# Declararando variáveis
cateto_oposto_inicial = input()
cateto_adjacente_inicial = input()

# Convertendo variáveis
cateto_oposto_convertido = float(cateto_oposto_inicial)
cateto_adjacente_convertido = float(cateto_adjacente_inicial)

# Resolvendo problemas
hipotenusa = (cateto_oposto_convertido ** 2) + (cateto_adjacente_convertido ** 2)
raiz_quadrada = sqrt(hipotenusa)

# Imprimindo o resultado de acordo com a saída desejada.
print("{:.2f}".format((raiz_quadrada)))
# print("{:.2f}".format((hipotenusa)))
