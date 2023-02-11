# Escreva um programa que pergunte a quantidade de km percorrridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0.15 km rodado.

# Zona de teste
# carro = "60" ~
# km_rodado = "0.15"#
# inicial_dias = "8" 
# inicial_km = "720" 

# Declarando variáveis
carro = input("Digite um valor de aluguel do carro por dia: ")
km_rodado = input("Digite um valor que vai valer pra cada KM rodado: ")
inicial_dias = input("Digite uma suposição de dias que se passaram: ")
inicial_km = input("Digite uma suposição de KM rodados pelo mesmo: ")

# Convertendo Variáveis 
convertido_valorCarro = int(carro)
convertido_kmRodado = float(km_rodado)
convertido_dias = int(inicial_dias)
convertido_km = int(inicial_km )

# Resolvendo problemas
valor_por_dias = convertido_valorCarro * convertido_dias
valor_km_rodado = convertido_kmRodado * convertido_km

# Imprimindo resultado de acordo com a saída desejada.
print("o valor por dias rodados é {} e o valor por km rodado é {} que resulta em R${:.2f} a pagar pelo aluguel.".format(valor_por_dias,valor_km_rodado, valor_por_dias + valor_km_rodado))




