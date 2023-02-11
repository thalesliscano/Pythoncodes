# -*- coding: utf-8 -*-
# Programa: copiappalavra2.py
# Programador:
# Data: 22/10/2012
# Este algoritmo lê uma palavra com pelo menos 5 caracteres, faz uma
# dos três últimos caracteres da palavra numa nova variável
# e imprime a palavra e a nova variável
# início do módulo principal
# descrição das variáveis utilizadas
# string palavra, partepala

# pré: palavra
palavra = input()
parte = palavra[-3:]
 


print("palavra = {} parte = {}".format(palavra,parte))





# pós: palavra partepal and partepal == palavra[tam-3:tam]
# fim do módulo principal