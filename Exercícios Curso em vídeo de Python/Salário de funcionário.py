'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10 %. Para salários inferiores ou iguais, o aumento é de 15%.'''

# Zona de teste 
# salario_funcionario_inicial = "9000"

# Declarando variáveis 
salario_funcionario_inicial = input()

#Convertendo variáveis 
salario_funcionario_convertido = float(salario_funcionario_inicial)

# Resolvendo os problemas proprostos 
#Calculando aumento salário superior a 1.250
aumento_salario_superior = salario_funcionario_convertido * 0.10 
soma_superior = aumento_salario_superior + salario_funcionario_convertido

#Calculando aumento de salário inferior a 1.250
aumento_salário_inferior = salario_funcionario_convertido * 0.15 
soma_inferior = aumento_salário_inferior + salario_funcionario_convertido

#Se o salário for maior que 1.250 ele vai mostrar o resultado de 10% de aumento
if salario_funcionario_convertido <= 1250:
  print("O aumento é de 15%, resultando num valor bruto de {}".format(soma_inferior))
else:
  print("O aumento é de 10%, resultando em um valor bruto de {}".format(soma_superior))

# Imprimir os resultado de acordo com a saída proposta.
print("-" * 60)
print(aumento_salario_superior)
