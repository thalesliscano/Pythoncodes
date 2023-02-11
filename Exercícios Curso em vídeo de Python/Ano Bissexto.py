'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4, deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;

Segunda situação: Se o ano de 2015 ou 2016 não for divisível por 4, então deveremos verificar se ele é divisível por 400. Se também não for divisível, o ano de 2015 não será bissexto;

Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4, então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.

'''

# Zona de teste 
# ano_qualquer_inicial = "2000"

#declarando variáveis 
ano_qualquer_inicial = input()

# Convertendo variáveis 
ano_qualquer_convertido = int(ano_qualquer_inicial)

#  Resolvendo o problema 
# Para saber se o ano é bissexto, temos que ver se ele é divísivel por 4 e 400 e não ser divísivel por 100.

primeira_divisao = ano_qualquer_convertido % 4 # tem que ser igual a 0
segunda_divisao = ano_qualquer_convertido % 100 # não tem que ser igual a 0
terceira_divisao = ano_qualquer_convertido % 400 # tem que ser igual a 0

cores = {
    "limpar":"\033[m",
    "brancoAzul":"\033[4;34m",
    "underline_Red":"\033[4:31m"
}
#Condicionais para saber se o ano é bissexto ou não 

if (ano_qualquer_convertido == primeira_divisao == 0 and segunda_divisao != 0) or terceira_divisao == 0 :
    print("Esse número é bissexto")
else:
    print("Esse ano não é bissexto")


print("A primeira divisão é {}0{}{}".format(cores ["brancoAzul"],primeira_divisao, cores["limpar"]))
print("A segunda divisão é  {}{}{}".format(cores ["brancoAzul"],segunda_divisao,cores["limpar"]))
print("A terceira divisão é {}{}{}".format(cores ["brancoAzul"],terceira_divisao,cores["limpar"]))
 
#  Exercício 32 COM CORES NA SAÍDA.