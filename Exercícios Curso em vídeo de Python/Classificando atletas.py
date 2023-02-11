'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR 
- Até 25 anos: SÊNIOR 
- Acima: Master'''

  # Declarando variáveis(ano de nascimento)
ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))

ano_atual = 2022
ver_idade = ano_atual - ano_de_nascimento

# Condicionais, vai informar de acordo com a idade do atleta, e vai classificando dependendo do ano de nascimento.
if ver_idade <= 9:
  print("Você possuí {} anos de idade, você é um atleta de categoria MIRIM".format(ver_idade))
elif ver_idade <= 14:
  print("Você possuí {} anos de idade, você é um atleta de categoria INFANTIL".format(ver_idade))
elif ver_idade <= 19:
  print("Você possuí {} anos de idade, você é um atleta de categoria JUNIOR".format(ver_idade))
elif ver_idade <= 25:
  print("Você possuí {} anos de idade, você é um atleta de categoria SÊNIOR".format(ver_idade))
elif ver_idade > 25:
  print("Você possuí {} anos de idade, você é um atleta de categoria MASTER".format(ver_idade))