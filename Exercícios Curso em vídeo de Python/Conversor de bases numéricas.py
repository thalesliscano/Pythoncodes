'''Escereva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal 
'''

# Declrando variável para escolher o tipo que vai ser  
from time import sleep


escolha_o_tipo = input('Digite um número inteiro: ')

# Convertendo variável
escolha_o_tipo_convertido = int(escolha_o_tipo)

# Escolha para qual você quer que o número colocado pelo mesmo seja convertido para as opções abaixo
print("Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] Converter para HEXADECIAMAL")
opcao = input()

# Condicionais, dependendo da escolha acima, vai ativar uma das condições para dar os respectivos valores convertidos.
if opcao == "1":
  escolha_o_tipo_convertido = bin(escolha_o_tipo_convertido)
  print("O número escolhido em Binario é {}".format(escolha_o_tipo_convertido[2::]))
elif opcao == "2":
  escolha_o_tipo_convertido = oct(escolha_o_tipo_convertido)
  print("O número escolhido em Octal é {}".format(escolha_o_tipo_convertido[2::]))
elif opcao == "3":
  escolha_o_tipo_convertido = hex(escolha_o_tipo_convertido)
  print("O número escolhido em Hexadecimal é {}".format(escolha_o_tipo_convertido[2::]))




# Vai pegar o valor das variáveis auxiliares


