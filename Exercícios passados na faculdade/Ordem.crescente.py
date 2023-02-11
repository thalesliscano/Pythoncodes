palavras_aleatoria_1,palavras_aleatoria_2,palavras_aleatoria_3,palavras_aleatoria_4  = map(str,input().split())

primeira_letra_1 = ord(palavras_aleatoria_1[0])
primeira_letra_2 = ord(palavras_aleatoria_2[0])
primeira_letra_3 = ord(palavras_aleatoria_3[0])
primeira_letra_4 = ord(palavras_aleatoria_4[0])

if primeira_letra_1 < primeira_letra_2 and primeira_letra_1 < primeira_letra_3 and primeira_letra_1 < primeira_letra_4:
  if primeira_letra_2 < primeira_letra_3 and primeira_letra_2 < primeira_letra_4:
    if primeira_letra_3 < primeira_letra_4:
      print("ordem crescente")
else:
  print("não estão em ordem crescente")

print(primeira_letra_1)
print(primeira_letra_2)
print(primeira_letra_3)
print(primeira_letra_4)

