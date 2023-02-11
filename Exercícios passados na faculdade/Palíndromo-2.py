algo = input().upper()
tam = len(algo)

msg = "palíndromo"
aux = ""

for i in algo[::-1]:
  aux += i
if algo == aux:
  print(msg)
else:
  msg = "não palíndromo"
  print(msg)