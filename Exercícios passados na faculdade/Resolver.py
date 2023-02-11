# Somando horas,minutos e segundos 

# Declarando e convertendo as variáveis
hora_1, minutos_1, segundos_1 = map(int,input().split())
hora_2, minutos_2, segundos_2 = map(int,input().split())


# Calculando as variáveis
# Calculando segundos
segundos = (segundos_1 + segundos_2)
total_segundos = segundos % 60

# Calculando minutos
minutos = minutos_1 + minutos_2 + (segundos // 60)
total_minutos = minutos % 60

# Calculando horas
horas = hora_1 + hora_2
total_horas = horas + (minutos // 60) 

# Imprimindo as informações de acordo com o formato pedidos
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos +'.format(hora_1, minutos_1, segundos_1))
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos ='.format(hora_2, minutos_2, segundos_2))
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos'.format(total_horas, total_minutos, total_segundos))
