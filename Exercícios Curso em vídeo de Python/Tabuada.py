# ler um número inteiro qualquer e fazer sua tabuada.

# Declrando variável
num = input("Digite um número: ")

# Convertendo variável
num = int(num)
# Resolvendo problemas
# Aqui euu crio as linhas da tabuada e faço cada uma receber o valor referente qual tabuada desejar, e multiplico pelos números de 1 a 10.
linha1 = num * 1
linha2 = num * 2
linha3 = num * 3
linha4 = num * 4
linha5 = num * 5
linha6 = num * 6
linha7 = num * 7
linha8 = num * 8
linha9 = num * 9
linha10 = num * 10

# Imprimindo o resultado de acordo com a saída desejada.
print(f"A tabuada deste número é:\n{num} X 1 = {linha1:2}\n{num} X 2 = {linha2:2}\n{num} X 3 = {linha3:2}\n{num} X 4 = {linha4:2}\n{num} X 5 = {linha5:2}\n{num} X 6 = {linha6:2}\n{num} X 7 = {linha7:2}\n{num} X 8 = {linha8:2}\n{num} X 9 = {linha9:2}\n{num} X 10 = {linha10:2} ")

