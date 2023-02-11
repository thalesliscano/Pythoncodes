
# estado das variáveis após a leitura
palavra = input("Digite uma palavra de 5 letras: ")
palavra_maiuscula = palavra.upper()
codificador = int(input("Um número entre 0 e 25: "))

# letraC = chr((ord(letra) - ord('A') + codificador)%26 + ord('A'))
# codifica os 5 caracteres da variável palavra
char0 = chr((ord(palavra_maiuscula[0]) - ord('A') + codificador)%26 + ord('A')) 
char1 = chr((ord(palavra_maiuscula[1]) - ord('A') + codificador)%26 + ord('A')) 
char2 = chr((ord(palavra_maiuscula[2]) - ord('A') + codificador)%26 + ord('A'))
char3 = chr((ord(palavra_maiuscula[3]) - ord('A') + codificador)%26 + ord('A')) 
char4 = chr((ord(palavra_maiuscula[4]) - ord('A') + codificador)%26 + ord('A'))

# concatena os caracteres codificados
codificada = char0 + char1 + char2 + char3 + char4

# estado da variável após a codificação
print(codificada)