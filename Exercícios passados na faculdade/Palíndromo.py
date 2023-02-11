algo_aleatorio = input().lower()

algo_aleatorio_ao_contrario = algo_aleatorio[::-1]

if  algo_aleatorio == algo_aleatorio_ao_contrario:
    print("palíndromo")
else:
    print("não palíndromo")