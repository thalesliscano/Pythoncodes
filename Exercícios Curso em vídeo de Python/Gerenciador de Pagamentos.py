'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista DINHEIRO/CHEQUE 10% de desconto
- À vista no cartão 5% de desconto 
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros

Exemplo de entrada: 
1500
1

Outro exemplo:
4000
4
10
'''
# Cores do programa
cores = {
    "limpar":"\033[m",
    "RedError":"\033[1;36m",
    "underline_Red":"\033[4:31;0m"
}

# Zona de teste
# valor_inicial = "4000"

# Declrando variáveis 
valor_inicial = input("Valor da conta inicial: ")

# Convertendo variáveis para ponto fluatuante (float)
valor_convertido = float(valor_inicial)

# FORMAS DE PAGAMENTO 
print("FORMAS DE PAGAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão ")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

# Escolher opções
escolha_um_opcao = input("Qual é a opção: ")

# Colocar as opções e implementar as contas dentro das condicionais, declarando as variáveis correspondidas pelas mesmas.
if escolha_um_opcao == "1":
    conta_desconto = (valor_convertido * 10) / 100
    valor_atualizado = valor_convertido - conta_desconto
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(valor_convertido, valor_atualizado))
elif escolha_um_opcao == "2":
    conta_desconto = (valor_convertido * 5) / 100
    valor_atualizado = valor_convertido - conta_desconto
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(valor_convertido, valor_atualizado))
elif escolha_um_opcao == "3":
    conta_parcela = (valor_convertido) / 2
    valor_atualizado = conta_parcela
    print("Sua compra de R${:.2f} vai custar duas parcelas de R${:.2f}".format(valor_convertido, valor_atualizado))
elif escolha_um_opcao == "4":
    # Declarar valor de parcela
    parcela = input("Vai parcelar em quantas vezes: ")
    # Converter valor de parcela pra float
    parcela_convertida = float(parcela)
    conta_parcela = (valor_convertido / parcela_convertida) * 1.20
    valor_final = (valor_convertido * 0.20) + valor_convertido
    print("Sua compra de R${:.2f} vai custar parcelas de R${:.2f}, tendo juros de 20%, obtendo um valor final de R${:.2f}".format(valor_convertido,conta_parcela, valor_final))
else:
  print("{}OPÇÂO INVÁLIDA DE PAGAMENTO{}".format(cores["RedError"],cores["limpar"]))