# -*- coding: utf-8 -*-
# Declarando variáveis e convertendo-as
leitura1,leitura2,leitura3,leitura4 = map(int,input().split())

leituras_media =  (leitura1 + leitura2 + leitura3 + leitura4) / 4
# Caso tenha qualidade boa
if leituras_media < 50:
  print("Qualidade do Ar Boa")
elif leituras_media >= 50 and leituras_media == 100:
  print("Qualidade do Ar Regular") 
elif leituras_media > 100 and leituras_media <= 200:
  print("Qualidade do Ar Inadequada") 
elif leituras_media > 200 and leituras_media < 300:
  print("Qualidade do Ar Ruim") 
elif leituras_media >= 300:
  print("Qualidade do Ar Péssima")

print(leituras_media)