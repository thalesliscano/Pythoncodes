# Criar um programa que consiga ver o quanto de dinheiro tem na carteira e mostre a conversão em dólares pra saber o quanto ela pode comprar.

# Declarando variáveis
inp_carteira = input("Quanto dinheiro você têm na carteira? R$")# Coloco o valor que tem na carteira
inp_dolar = input("Quanto que ta o dolár: U$")# Aqui eu coloco o valor do dólar 

# Convertendo variáveis para o tipo
# Depois eu atribui o valor de carteira e dólar para variável dinheiro e dolar
dinheiro = float(inp_carteira)
dolar = float(inp_dolar)

# Resolvendo variáveis
# Divido dinheiro por dolar pra achar quantidade de dolar que posso comprar
converter = dinheiro / dolar

# Imprimindo resultados de acordo com a saída desejada.
print("Tendo {} na carteira você pode comprar {:.2f} dólares".format(dinheiro, converter))
