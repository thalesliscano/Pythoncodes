''' Escreva um programa para aprovar o empréstimo bancário para a compra de um casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

# Zona de teste


# Zona de teste
# valor_casa_inicial = "80000"
# salario_comprador_inicial = "1600"
# anos_financiamento  = "7"

# Declarando variáveis
valor_casa_inicial = input("Digite do imóvel: ")
salario_comprador_inicial = input("Digite salário do comprador: ")
anos_financiamento = input("Digite em quantos anos vai ser financiado: ")

# Convertendo variáveis 
valor_casa_convertido = float(valor_casa_inicial)
salario_comprador_convertido = float(salario_comprador_inicial)
anos_para_quitar_convertido = int(anos_financiamento)

# Resolvendo problemas 
# Aqui vou fazer a conta pra achar quanto vale os 30% do salário
trinta_procento_salario = (salario_comprador_convertido) * (30 / 100)  #480,00
valor_mensal = valor_casa_convertido / (anos_para_quitar_convertido * 12) #952.38

print("Seu salário sendo R${:.2f}, a amortização tendo com limite 30%, seu limite será R${:.2f}.".format(salario_comprador_convertido, trinta_procento_salario))
# Condicioanis para ver se o pedido de financiamento será aprovado.
if valor_mensal > trinta_procento_salario:
    print("Desculpe, seu pedido foi negado, pois o valor de cada parcela seria R${:.2f}.".format(valor_mensal))
    
else: 
    print("Ah, parabéns seu pedido foi aprovado!!! Em {} anos você pagara R${:.2f} por mês.".format(anos_para_quitar_convertido,valor_mensal))




# PrintTest
# print(trinta_procento_salario)
# print(f" {valor_mensal}" )

# EXE 36 curso em video.