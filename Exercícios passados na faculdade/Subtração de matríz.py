# Programador: Thales Liscano Carvalho
# Data: 28/11/2022
# Descrição: A entrada é dada por um bloco de linhas. A primeira linha contêm dois números inteiros
# m e n indicando as dimensões da matriz, seguido de 2*m linhas com n números cada. As primeiras m linhas
# representam as linhas da matriz a e as m últimas linhas representam as linhas da matriz b. 
# A saída consiste em imprimir uma lista de listas representado a matriz subtração c do par de matrizes
# da entrada.
# Declarando o tamanho da matriz(Linhas x Colunas)
linhas,colunas = map(int,input().split())

# Declarando as dimensões das matrizes A, B  e matrizC com valores 0 em cada índices.
A = [[0]*colunas for i in range(linhas)]
B = [[0]*colunas for i in range(linhas)]
matrizC = [[0]*colunas for i in range(linhas)]

tam = len(A)
# Trocar valores das matrizes A e B
matrizA = [0]*linhas
matrizB = [0]*linhas

for i in range(tam):
  matrizA[i] = list(map(int,input().split())) 

for i in range(tam):
  matrizB[i] = list(map(int,input().split()))

subtracao = 0
# Deixo os índices das linhas parados para que #possoa fazer a subtração por colunas, #exemplo:Matriz 2x2 | 1 volta(j) - [0][0], 2 volta(j) - [0][1], 3 volta(j) - [1][0], 4 volta(j) [1][1] 
for i in range(linhas):
  for j in range(colunas):
    subtracao = matrizA[i][j] - matrizB[i][j]
    matrizC[i][j] = subtracao
    subtracao = 0
# print cada uma das linhas
for i in range(linhas):
  print("{}".format(matrizC[i])) 