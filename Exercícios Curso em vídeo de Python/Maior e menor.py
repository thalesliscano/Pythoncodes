'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

# Zona de teste 
# numero_um_inicial = "5"
# numero_dois_inicial = "7"
# numero_tres_inicial = "2"

# Declarando variáveis 
numero_um_inicial = input()
numero_dois_inicial = input()
numero_tres_inicial = input()


# Convertendo variáveis 
numero_um_convertido = int(numero_um_inicial) 
numero_dois_convertido = int(numero_dois_inicial) 
numero_tres_convertido = int(numero_tres_inicial)

# Descobrindo numero maior entre os três valores 
if numero_um_convertido > numero_dois_convertido and numero_um_convertido > numero_tres_convertido:
    print("O numero maior é {}".format(numero_um_convertido))
elif numero_dois_convertido > numero_um_convertido and numero_dois_convertido > numero_tres_convertido:
    print("O número maior é {}".format(numero_dois_convertido))
elif numero_tres_convertido > numero_um_convertido and numero_tres_convertido > numero_dois_convertido:
    print("O número maior é {}".format(numero_tres_convertido))
else: 
    print("Os números são todos iguais")

# Descobrindo o numero menor entre os três
if numero_um_convertido < numero_dois_convertido and numero_um_convertido < numero_tres_convertido:
    print("O numero menor é {}".format(numero_um_convertido))
elif numero_dois_convertido < numero_um_convertido and numero_dois_convertido < numero_tres_convertido:
    print("O número menor é {}".format(numero_dois_convertido))
elif numero_tres_convertido < numero_um_convertido and numero_tres_convertido < numero_dois_convertido:
    print("O número menor é {}".format(numero_tres_convertido))
else: 
    print("Os números são todos iguais")

