#-*- coding: utf-8 -*-
# Programa: perimetroareaTI.py
# Programador:
# Data: 23/08/2020
# Este programa lê o valor da base e o lado de um
# triângulo isósceles, calcula e imprime o perímetro e a
# área do triângulo no formato especificado.
# declaração das bibliotecas utilizadas
from math import sqrt
# início do módulo principal
# descrição das variáveis utilizadas
# float base, lado, perimetro, area

# pré: base lado

# Passo 1. Leia a base e os catetos do triângulo isósceles
print('Entre com os valores dos lados do triângulo: ')
base = float(input())
lado = float(input())
# Passo 2. Calcule o perímetro e a área do triângulo
# Passo 2.1. Calcule o perímetro do triângulo
perimetro = (lado * 2) + base
# Passo 2.2. Calcule a área do triângulo
# Passo 2.1.1. Calcule o valor da altura
altura = (lado ** 2) - ((base / 2) ** 2)
altura_raiz = altura ** 1/2
area = (base + altura_raiz) / 2 
# Passo 3. Imprima o perímetro e área
print(altura)
print(altura_raiz)
print("Perímetro = {:.2f}\nÁrea = {:.2f}".format(perimetro,area))

# pós: perimetro == catetoop + catetoad + hipotenusa and
#      area == (catetoop*catetoad)/2.0
# fom do módulo principal