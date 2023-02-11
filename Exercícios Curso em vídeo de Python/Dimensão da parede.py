# Exercício de pintar a parede, aonde vou calcular a dimensão da parede e quanto de tinta devo usar para pintá-la.

# Declrando variáveis
inp_larguraParede = input() 
inp_alturaParede = input()

# Convertendo variáveis
largura = float(inp_larguraParede)
altura = float(inp_alturaParede)

# Resolvendo problemas
soma = (largura * altura) 

# Imprimindo resultado de acordo com a saída desejada.
print("A área dessa parede é: {}\n e a quantidade de tinta usada para pintar ela é: {} ".format(soma, soma / 2))