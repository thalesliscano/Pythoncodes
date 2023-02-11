# -*- coding: utf-8 -*-
# Somando horas,minutos e segundos 

# Declarando e convertendo as variáveis
horas_1, minutos_1, segundos_1 = map(int,input().split())
horas_2, minutos_2, segundos_2 = map(int,input().split())


# Calculando as variáveis
# Calculando segundos
segundos = (segundos_1 + segundos_2)
total_segundos = segundos % 60

# Calculando minutos
minutos = minutos_1 + minutos_2 + (segundos // 60)
total_minutos = minutos % 60

# Calculando horas
horas = horas_1 + horas_2
total_horas = horas + (minutos // 60) 
if  total_horas < 360:
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos +'.format(horas_1, minutos_1, segundos_1))
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos ='.format(horas_2, minutos_2, segundos_2))
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos'.format(total_horas,total_minutos,total_segundos))
elif total_horas >= 360:
    total_horas = 0
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos +'.format(horas_1, minutos_1, segundos_1))
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos ='.format(horas_2, minutos_2, segundos_2))
    print('{0:3d} Horas {1:2d} Minutos {2:2d} Segundos'.format(total_horas,total_minutos,total_segundos))

# Passo 3. Imprima a soma

