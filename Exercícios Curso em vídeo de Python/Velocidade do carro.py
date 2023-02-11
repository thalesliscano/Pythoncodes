'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar 7.00 por km acima do limite'''

# Declrando variáveis 
velocidade_carro_inicial = input()

# Convertendo variável
velocidade_carro_convertida = int(velocidade_carro_inicial)

# Resolvendo problemas
muta = (velocidade_carro_convertida - 80) * 7

# COndicioanal para ver se vai receber a muta ou não 
if velocidade_carro_convertida > 80:
  print("você foi mutado, o valor da multa a pagar é R${},00".format(muta))
else:
  print("Dirija com cuidado!!!")