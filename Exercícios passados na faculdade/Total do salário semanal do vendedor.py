# -*- coding: utf-8 -*-
# Programa: vendas.py
# Programador:
# Data: 28/11/2022
# A entrada é dada por um bloco, onde a primeira linha do bloco é dada por dois números inteiros 
# (num e prod) indicando o número de vendedores (vend) e a quantidade de itens (prod) comercializados
# por cada filial, seguido de num linhas da tabela representando as vendas de cada um dos i vendedores 
# 0<i<=num para cada um dos prod itens comercializados, seguido de uma linha com os valores de venda de 
# cada um dos prod itens. A saída consiste em imprimir uma tabela, onde cada linha contém o número do 
# vendedor com o respectivo salário semanal de cada vendedor da companhia.

#  Num. Vend. 	 Num. Item 
#    	            1 	 2 	 3 	 4 	 5 
#  1 	            10 	 4 	 5 	 6 	 7 
#  2 	            7 	 0 	 12 	 1 	 3 
#  3 	            4 	 9 	 5 	 0 	 8 
#  4 	            3 	 2 	 1 	 5 	 6 
#Obs: Os comentários não fazem parte da entrada, servem apenas para facilitar a compreensão do exercício
# Declarando linhas e colunas
linhas,colunas = map(int,input().split())

#Declarando a extensão da matriz
mat = [[0]*colunas for i in range(linhas)]

# Substituindo valores 
for j in range(linhas):
  mat[j] = list(map(int,input().split()))

# Declarando tabela de preços
tab_preco = list(map(int,input().split()))

# Convertendo valores da tabelo de preços para 10%, ja que os funcionário ganham 10% de cada venda.
for i in range(colunas):
  tab_preco[i] = tab_preco[i] * 0.10

soma_mat = [0] * linhas
for i in range(linhas):
  soma = 0
 
  for j in range(colunas):
    mat[i][j] = mat[i][j] * tab_preco[j]
    soma = soma + mat[i][j]
    soma_mat[i] = soma + 200
  if soma_mat[i] < 999:
    print("{0:2d}  {1:6.2f}".format(i+1,soma_mat[i]))
  else:
    print("{0:2d} {1:7.2f}".format(i+1,soma_mat[i]))


# fim do módulo principal