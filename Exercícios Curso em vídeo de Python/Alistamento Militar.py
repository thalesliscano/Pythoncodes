'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamnto.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


# Declarando variáveis 
from gettext import find

# Analisando se a pessoa é homem ou mulher.
vendo_o_sexo = input("Você é homem ou mulher: ")
if vendo_o_sexo == "homem":
  # Declarando variáveis(ano de nascimento)
  ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))

  ano_atual = 2022

    # Conta de anos
  ver_idade = ano_atual - ano_de_nascimento

  # Condicionais, vai informar se ele ainda vai se alistar
  if ver_idade < 18:
    quantos_anos_falta = abs(ver_idade - 18) 
    print("Você tem {} anos, ainda falta {} ano para o alistamento".format(ver_idade,quantos_anos_falta))
  elif ver_idade > 18:
    quantos_anos_atrasou = abs(ver_idade - 18)
    print("Você tem {} anos, está tendo um atraso de {} anos para o alistamento.".format(ver_idade,quantos_anos_atrasou))
  elif ver_idade == 18:
    print("Chegou a hora, com {} anos você vai se alistar no ano de {}".format(ver_idade,ano_atual))
elif vendo_o_sexo == "Eu quero":
  # Declarando variáveis(ano de nascimento)
  ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))

  ano_atual = 2022
    # Conta de anos
  ver_idade = ano_atual - ano_de_nascimento

  # Condicionais, vai informar se ele ainda vai se alistar
  if ver_idade < 18:
    quantos_anos_falta = abs(ver_idade - 18) 
    print("Você tem {} anos, ainda falta {} anos para o alistamento".format(ver_idade,quantos_anos_falta))
  elif ver_idade > 18:
    quantos_anos_atrasou = abs(ver_idade - 18)
    print("Você tem {} anos, está tendo um atraso de {} anos para o alistamento.".format(ver_idade,quantos_anos_atrasou))
  elif ver_idade == 18:
    print("Chegou a hora, com {} anos você vai se alistar no ano de {}".format(ver_idade,ano_atual))

  # Vai não vai dar o valor, mas vai dar um outra opção caso a pessoa queria continuar
elif vendo_o_sexo != "Eu quero" or "homem":
  print('Não é obrigatório, caso queira continuar, retorne o programa e em vez das duas opção, diga "Eu quero"')
# Ano atual
