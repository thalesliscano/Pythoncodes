from math import ceil, floor
# Declarando variável 
rga = input()

notaProvaUm = float(input("Digite a nota da primeira prova: "))
notaProvaDois = float(input("Digite a nota da segunda prova: "))
notaProvaTres = float(input("Digite a nota da terceira prova: "))
notaTrabalhoUm = float(input("Digite a nota do primeiro trabalho: "))
notaTrabalhoDois = float(input("Digite a nota do segundo trabalho: "))

pergunta_da_po = input("Fez a PO: ").upper()

if pergunta_da_po == "S":
  provaOpitativa = float(input("Digite a nota: "))
  menorNota = notaProvaUm
  if provaOpitativa > notaProvaUm:
    notaProvaUm = provaOpitativa
  if provaOpitativa > notaProvaDois:
    notaProvaDois = provaOpitativa
  if provaOpitativa > notaProvaTres:
    notaProvaTres = provaOpitativa
    # Calculando a média depois de trocar os valores
    msg = ""
    mediaDasProvas = (notaProvaUm + notaProvaDois + notaProvaTres) // 3
    mediaDosTrabalhos = (notaTrabalhoUm + notaTrabalhoDois) // 2
    mediaFinal = ceil(((mediaDasProvas + mediaDosTrabalhos) / 2))
    if mediaFinal >= 6.0:
      msg = "AP"
      print('{}: Média ={:5.1f} - {}'.format(rga,mediaFinal,msg))
    else:
      msg = "RP"
      print('{}: Média ={:5.1f} - {}'.format(rga,mediaFinal,msg))
else:
  msg = ""
  mediaDasProvas = (notaProvaUm + notaProvaDois + notaProvaTres) / 3.0
  mediaDosTrabalhos = (notaTrabalhoUm + notaTrabalhoDois) / 2.0
  mediaFinal = floor(((mediaDasProvas + mediaDosTrabalhos) / 2.0))
  if mediaFinal > 6.0:
    msg = "AP"
    print('{}: Média ={:5.1f} - {}'.format(rga,mediaFinal,msg))
  else:
    msg = "RP"
    print('{}: Média ={:5.1f} - {}'.format(rga,mediaFinal,msg))
