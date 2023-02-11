'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$o,50 por km para viagens de até 200km e R$0,45 para viagens mais longas'''

# Declarando variáveis
distancia_viagem_inicial = input()

# Convertendo variável
distancia_viagem_convertida = int(distancia_viagem_inicial)

# Resolvendo problemas
valor_viagem_normal = distancia_viagem_convertida * 0.50
valor_viagem_longa = distancia_viagem_convertida * 0.45

# Condicional para ver qual preço será cobrado dependendo da distanciância
if distancia_viagem_convertida <= 200:
  print("A distância percorrida foi {}, o preço a pagar é R${},00".format(distancia_viagem_convertida,valor_viagem_normal))
else:
  print("A distância percorrida foi {}, o preço a pagar é R${},00".format(distancia_viagem_convertida,valor_viagem_longa))


