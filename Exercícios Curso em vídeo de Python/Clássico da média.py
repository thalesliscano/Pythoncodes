'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

# Declarando variáveis 
nota1 = input("Digite sua nota: ")
nota2 = input("Digite sua nota: ")
nota3 = input("Digite sua nota: ")
nota4 = input("Digite sua nota: ")

# Convertendo variáveis
primeira_nota = float(nota1)
segunda_nota = float(nota2)
terceira_nota = float(nota3)
quarta_nota = float(nota4)

# Somando as notas 
soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota

# Dividindo as notas
media = soma / 4 

# Condicioanis para ver se o aluno foi APROVADO ou REPROVADO 
if media <= 5.0:
  print("ALUNO REPROVADO")
elif media <= 6.9:
  print("ALUNO REPROVADO")
elif media >= 7.0:
  print("ALUNO APROVADO")