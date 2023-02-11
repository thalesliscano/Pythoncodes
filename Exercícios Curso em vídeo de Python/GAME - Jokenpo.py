'''Crie um programa que faça o computador jogar jokenpô com você'''


from random import randint
from time import sleep
# Opções para escolher a jogada
print('''Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

# Cores do placar
cor = {
  "DERROTA/ERRO":"\033[31m",
  "VITÓRIA/MENSAGEM":"\033[32m",
  "EMPATE":"\033[33m",
  "LIMPAR":"\033[m"
}

# Declarando variáveis e convertendo
# Jogada do jogador
jogada_jogador = int(input("Qual é sua jogada: "))
print("-=" * 10)
sleep(0.5)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
print("-=" * 10)

# COndicional da jogado do jogador
if jogada_jogador == 0:
  print("Jogador jogou PEDRA")
elif jogada_jogador == 1:
  print("Jogador jogou PAPEL")
elif jogada_jogador == 2:
  print("Jogador jogou TESOURA")
else:
  print("{}ERRO, por favor escolha uma das opções acima!{}".format(cor["DERROTA/ERRO"],cor["LIMPAR"]))

# Jogada do computador
jogada_computador = randint(0,2)

# Condicional da jogada do computador
if jogada_jogador != 0 and jogada_jogador != 1 and jogada_jogador != 2:
  print("{}Computador não conseguiu entender jogada...{}".format(cor["VITÓRIA/MENSAGEM"],cor["LIMPAR"]))
elif jogada_computador == 0:
  print("Computador jogou PEDRA")
elif jogada_computador == 1:
  print("Computador jogou PAPEL")
elif jogada_computador == 2:
  print("Computador jogou TESOURA")

# Condicional de vitório, derrota e empate entre o computador e o jogador
if (jogada_jogador == 0 and jogada_computador == 1) or (jogada_jogador == 1 and jogada_computador == 2) or (jogada_jogador == 2 and jogada_computador == 0):
  print("{}COMPUTADOR VENCE{}".format(cor["DERROTA/ERRO"],cor["LIMPAR"]))
elif (jogada_jogador == 1 and jogada_computador == 0) or (jogada_jogador == 2 and jogada_computador == 1) or (jogada_jogador == 0 and jogada_computador == 2):
  print("{}JOGADOR VENCE{}".format(cor["VITÓRIA/MENSAGEM"],cor["LIMPAR"]))
elif (jogada_jogador == 0 and jogada_computador == 0) or (jogada_jogador == 1 and jogada_computador == 1) or jogada_jogador == 2 and jogada_computador == 2:
  print("{}EMPATE!!!!{}".format(cor["EMPATE"],cor["LIMPAR"]))


