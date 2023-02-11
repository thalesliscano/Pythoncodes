'''Faça um progrma que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
  ex: Ana Maria de Souza
  primeiro = Ana
  último = Souza'''

# Zona de teste
# nome_completo = "Thales Liscano Carvalho Filho".split()

# Declarando problemas
nome_completo = input().strip().split()
# Resolvendo problemas
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

# Imprimindo as informações de acordo com o pedido de saída 
print("O primerio nome é: {}".format(primeiro_nome))
print("O último nome é: {}".format(ultimo_nome))

