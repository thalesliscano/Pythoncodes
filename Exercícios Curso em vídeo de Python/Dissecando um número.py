'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
EX: Digite um número: 1834
Unidade: 4   Dezena: 3  Centena: 8  Milha: 1
'''

# Zona de teste
# numero_inicial = "1834"

# Declarando variável

numero_inicial = input()

# Convertendo variável
numero_convertido = int(numero_inicial)

# Começar a procurar as unidades 
# Vou pegar o valor dessa variável convertida e ir pegando o resto da divisão para ir pegando um por um
unidade = numero_convertido % 10
# Continuando, procurar o valor de dezena
# Daqui em diante temos que pegar divisão inteiro do numero_inicial, pra assim pegar o resto da divisão referente a casa que estamos procurando que nestre primeiro caso é a dezena, posteriormente centena e milhar.
dezena = (numero_convertido // 10) % 10


# Procurar o valor de centena 
centena = (numero_convertido // 100) % 10

# Procurar milhar
milhar = (numero_convertido // 1000) % 10

print(unidade)
# Imprimindo o resultado de acordo com a saída desejada.
# print("Unidade: {}\nDezena: {}\nCentena:{}\nMilhar: {}".format(unidade,dezena,centena,milhar))
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade,dezena,centena,milhar))



