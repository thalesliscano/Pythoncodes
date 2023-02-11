#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Zona de teste
# inicial_salario = "4319.43"

# Declrando variáveis
inicial_salario = input("Digite um valor: R$ ")
inicial_aumento = input("Quantos porcentos:  ")

# Convertendo variáveis
convertido_salario = float(inicial_salario)
convertido_aumento = float(inicial_aumento)

# Resolvendo problemas
conta = convertido_salario * convertido_aumento / 100 

# Imprimindo o resultado de acordo com a saída desejada.
print("O funcionário que ganha R${:.2f} reais, depois do aumento vai passar a ganha R${:.2f}".format(convertido_salario, conta + convertido_salario))
