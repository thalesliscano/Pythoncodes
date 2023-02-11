# -*- coding: utf-8 -*-
# Programa: medianotas4.py
# Programador:
# Data: 25/11/2016
# Este programa calcula a média final de um aluno para
# um curso com o total de três notas de provas e duas notas de trabalhos.
# A média da disciplina é dada por 0.75 da média das provas somada com
# 0.25 da média dos trabalhos. O alunos pode fazer uma prova optativa
# que substitui a menor nota das provas. Caso a média do aluno seja maior 
# ou igual a 6.0 o aluno e se o aluno tiver frequê3ncia superior a 75%
# o aluno é considerado aprovado ('AP'), caso contrário, o aluno é considerado
# reprovado ('RP'). Se o total de faltas for superior a 25% o aluno é
# considerado reprovado por falta ('RF').
# início do módulo principal
# descrição das variáveis utilizadas
# float prova1, prova2, prova3, trab1, trab2, opt
# float menornota, somaProvas, somaTraba
# flroat mediaProvas, mediaTraba, mediaFinal
# int freq
# str rga, resp

# pré: rga prova1 prova2 prova3 trab1 trab2 freq resp opt

# Passo 1. Leia as notas das provas e trabalhos
# Passo 1.1. Leia a matrícula e as notas
rga = input()
prova1 = float(input())
prova2 = float(input())
prova3 = float(input())
# Passo 1.2. Leia as notas dos trabalhos.
notaTrabalhoUm = float(input())
notaTrabalhoDois = float(input())
# Passo 1.3. Leia a porcentagem da frequência
freq = int(input())
# Passo 1.4. Pergunte se o aluno fez a prova opitativa, caso sim, troque pela menor nota do aluno e faça a conta das provas.
conta_prova = 0
pergunta_opitativa = input().lower()
if pergunta_opitativa == "s":
    prova_opitativa = float(input())
    if prova1 < prova2 and prova1 < prova3:
      prova1 = prova_opitativa
      conta = (prova1 + prova2 + prova3) // 3
    elif prova2 < prova1 and prova2 < prova3:
      prova2 = prova_opitativa
      conta = (prova1 + prova2 + prova3) // 3
    elif prova3 < prova1 and prova3 < prova2:
      prova3 = prova_opitativa
      conta_prova = (prova1 + prova2 + prova3) // 3
    elif prova1 == prova2 == prova3 == prova1:
      conta_prova = (prova1 + prova2 + prova3) // 3
# Calcule o trabalho

conta_trabalho = (notaTrabalhoUm + notaTrabalhoDois) // 2
# Passo 2.3. Calcule a Menor Nota
media_final = round((conta_prova + conta_trabalho) / 2,1)

if media_final >= 6.0 and freq >= 75:
  msg = "AP"
  print('{0:s}: Média ={1:5.1f}, Frequência ={2:4d}% - {3:s}'.format(rga,media_final,freq,msg))
else:
  msg = "RP"
  print('{0:s}: Média ={1:5.1f}, Frequência ={2:4d}% - {3:s}'.format(rga,media_final,freq,msg))
# Passo 2.8. Faça um arredondamento na média final com uma casa decimal
# Passo3. Compute a mensagem correspondente 

# Passo 3. Imprima os resultados
# print('{0:s}: Média ={1:5.1f}, Frequência ={2:4d}% - {3:s}'.format(rga,mediaFinal,freq,msg))

# pós: menorNota == min{prova1, prova2, prova3} and
#      ((mediaFinal == 0.75*(prova1+prova2+prova3)/3.0 + 
#      0.25*(trab1+trab2)/2.0) or
#      (mediaFinal == 0.75*(prova1+prova2+prova3-menorNota+opt)/3.0
#      + 0.25*(trab1+trab2)/2.0)) and ((mediaFinal >=6.0 and 
#      freq >= 75 and 'AP') or (mediaFinal < 6.0 
#      and freq >= 75 and 'RN') or (freq < 75 and 'RF'))
# fim do módulo principal
