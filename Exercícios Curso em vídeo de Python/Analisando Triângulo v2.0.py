'''Desenvolva um programa que leia o comprimento de três retas e diga oa usuário se elas podem ou não formar um triângulo.
Exemplo de entrada:
3.5
2.75
4
Saída:
podem formar 

Outro exemplo de entrada:
2
4
9
Sáida:
Não podem formar
'''
# Variáveis testes:
# primeiro_segmento = "2"
# segundo_segmento = "3"
# terceiro_segmento = "4"

# Declarando variáveis 
primeiro_segmento = input()
segundo_segmento = input()
terceiro_segmento = input()

# Convertendo variáveis 
primeiro_segmento_convertido = float(primeiro_segmento)
segundo_segmento_convertido = float(segundo_segmento)
terceiro_segmento_convertido = float(terceiro_segmento)

'''Para formar um triãngulo deve se entender a seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Veja o resumo da regra abaixo:

| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''
# Conta dos triângulos para ter os segmentos com condições
# Modulo referente ao primeiro segmento
modulo_um = segundo_segmento_convertido - terceiro_segmento_convertido

# Modulo referente ao segundo segmento
modulo_dois = primeiro_segmento_convertido - terceiro_segmento_convertido

# Modulo referente ao terceiro segmento
modulo_terceiro = primeiro_segmento_convertido - segundo_segmento_convertido

# Soma dos segmento
# Soma referente ao primeiro segmento
soma_um = segundo_segmento_convertido + terceiro_segmento_convertido

# Soma referente ao segundo segmento
soma_dois = primeiro_segmento_convertido + terceiro_segmento_convertido

# Soma referente ao terceiro segmento
soma_tres = primeiro_segmento_convertido + segundo_segmento_convertido

# Aqui ele vai analisar através da regra se pode ou não formar um triângulo
if modulo_um < primeiro_segmento_convertido < soma_um and modulo_dois < segundo_segmento_convertido < soma_dois and modulo_terceiro < terceiro_segmento_convertido < soma_tres:
    print("Podem formar um triângulo!!!")
else: 
    print("Não podem formar um triângulo!!")

    # Esse é referente ao equilátero (as medidas dos seus lados são todas congruentes)
if primeiro_segmento_convertido == segundo_segmento_convertido and segundo_segmento_convertido == terceiro_segmento_convertido and terceiro_segmento_convertido == primeiro_segmento_convertido:
        print("FORMA UM TRIÂNGULO EQUILÁTERO")

    # Esse é referente ao Isóceles (possui exatamente dois lados congruentes)
elif (primeiro_segmento_convertido == segundo_segmento_convertido != terceiro_segmento_convertido) or (segundo_segmento_convertido == terceiro_segmento_convertido != primeiro_segmento_convertido) or (terceiro_segmento_convertido == primeiro_segmento_convertido != segundo_segmento_convertido):
        print("FORMAR UM TRIÂNGULO ISÓCELES")

    # Esse é referente ao escaleno (todos os lados com medidas distintas)
elif primeiro_segmento_convertido != segundo_segmento_convertido and segundo_segmento_convertido != terceiro_segmento_convertido and terceiro_segmento_convertido != primeiro_segmento_convertido:
        print("FORMAR UM TRIÂNGULO ESCALENO")