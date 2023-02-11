palavra = input()
# valor_numerico_str = len(palavra)
igual = 0
aux = 1
aux1 = 0 
aux3 = 0


# r = ord()
# letras = 0
# while r > 0:
#   letras = r % 10
#   r += -1
# for r in palavra:


while True:
  # print(aux, valor_numerico_str)
  if aux == len(palavra):  
    print("quebro")
    break
  aux2 = palavra[aux1]# h
  aux3 = palavra[aux]# h
  if aux2 == aux3:
    igual += 1  
  aux1 += 1
  aux += 1
  # valor_numerico_str += -1

print(igual)
# print(aux1)
