'''Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal 
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida

Exemplo de entrada:
1.97
87
Saída:
PARABÉNS, você está na faixa de PESO NORMAL!
Exemplo de saída:
1.60
150
Saída:
Você está em OBESIDADE MÓRBIDA, cuidado!!!!

O índice é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado.
'''
# Zona de teste
# peso_inicial = "87"
# altura_inicial = "1.97"

# Declarando variável
altura_inicial = input("Qual sua altura: ")
peso_inicial = input("Qual seu peso: ")


# Convertendo variáveis para ponto flutuante(float)
altura_convertida = float(altura_inicial)
peso_convertido = float(peso_inicial)

# Conta do IMC de acordo com a lógica apresentada anteriormente logo após os exemplos de entra e saída
calculo_imc = peso_convertido / (altura_convertida ** 2)

# Condicional para ver em qual categoria de peso a pessoa se encontra 
if calculo_imc < 18.5:
  print("Você está ABAIXO DO PESO, cuidado!!\nSeu IMC: {:.2f}".format(calculo_imc))
elif calculo_imc <= 25.0:
  print("PARABÉNS, você está na faixa de PESO NORMAL!!\nSeu IMC: {:.2f}".format(calculo_imc))
elif calculo_imc <= 30.0:
  print("Você está na faixa de SOBRE PESO\nSeu IMC: {:.2f}".format(calculo_imc))
elif calculo_imc <= 40.0:
  print("Você se encontra na faixa de OBESIDADE, preste atenção!!!\nkSeu IMC: {:.2f}".format(calculo_imc))
elif calculo_imc >= 40.0:
  print("Você está em OBESIDADE MÓRBIDA, cuidado!!!!\nSeu IMC: {:.2f}".format(calculo_imc))

# print de depuração de variáveis
# print("{:.2f}".format(calculo_imc))
