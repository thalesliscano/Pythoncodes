# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Declrando variáveis
inicial_produto = input()
inicial_desconto = input()

# Convertendo variáveis
convertido_produto = float(inicial_produto)
convertido_desconto = float(inicial_desconto)

# Resolvendo problemas
conta = (convertido_desconto * convertido_produto) / 100 # Aqui ele vai multiplicar o valor com o produto e dividir por 100, para em seguida
valor_final = convertido_produto - conta                 # Eu pegar o valor de conta e subtrair pelo produto pra saber o valro final 

print('O valor inicial do produto é R${:.2f},sendo "5%" de desconto que equivale a R${:.2f}, o valor final corresponde a R${:.2f}'.format(convertido_produto, conta, valor_final))

