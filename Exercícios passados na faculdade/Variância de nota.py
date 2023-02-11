# '''Esse programa vai mostrar o intervalo de variação da maior e menor nota'''


# # Declarando variáveis 
nota1, nota2, nota3, nota4 = map(float, input().split())


maiorNota = 0
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:
  maiorNota = nota1
elif nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
  maiorNota = nota2
elif nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
  maiorNota = nota3
elif nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
  maiorNota = nota4
elif nota1 == nota2 == nota3 == nota4 == nota1:
    maiorNota = 0
# menor nota
menorNota = 0
if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    menorNota = nota1
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    menorNota = nota2
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    menorNota = nota3
elif nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    menorNota = nota4
elif nota1 == nota2 == nota3 == nota4 == nota1:
    maiorNota = 0
intervalo = maiorNota - menorNota
print(maiorNota)
print(menorNota)
print(intervalo)


