'''Faça um programa que leia uma frase pelo teclado e mostre: 
  Quantas vezes aparece a letra "A"
  Em que posição ela aparece a primeira vez
  Em que posição ela aprece a última vez'''

  #Zona de teste 
# frase_incial = "  Amanda Nunes Amor".strip()

# Declarando variáveis 
frase_incial = input().strip()

# Resolvendo problemas
convertendo_frase = frase_incial.casefold()
conta_frase = convertendo_frase.count("a",0,)
primeira_posicao = convertendo_frase.find("a")+1
ultima_posicao = convertendo_frase.rfind("a")+1

#Imprimindo as informações 
print('Quantas vezes aparece a letra "A": {}'.format(conta_frase))
print("Em que posição ela aparece a primeira vez: {}".format(primeira_posicao))
print("Em que posição ela aprece a última vez: {}".format(ultima_posicao))