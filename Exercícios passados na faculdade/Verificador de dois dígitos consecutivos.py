'''Dados um número inteiro num, verificar se num possui dois dígitos consecutivos iguais. Imprimir a mensagem 'sim' caso num tenha dois dígitos consecutivos iguais e 'não' caso contrário.

A entrada é dada por um número inteiro. A saída é consiste em imprimir a mensagem 'sim' caso o número possua dois dígitos consecutivos iguais e a mensagem 'não' caso contrário.

Neste exercício não pode ser usado listas, strings ou arranjos.'''


# Declarando variáveis e convertendo-as
num = int(input())
# aux = num
digitos = 0
# arm = 0
num_1 = 0

# Uma condição para ver se o número tem mais mais de um digíto 
if num > 9:
  # Esse while vai pegar digíto por digíto 
  while num > 0:
    soma = num % 10 # Vai pegar o menos significante
    num = num // 10 # Vai atualizar a variável
    num_1 = soma # Vai pegar o menos significante do próximo

# Vai comprar o último com o penúltimo e assim por diante, caso tenha um igual ele já vai cessar pra resposta sem precisar conferir os outros.
    if soma == num_1:
      break
    digitos += 1
  if soma == num_1:
    print("sim")
  else:
    print("não")
else:
  print("não")
  

