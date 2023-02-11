#Tava aprendendo sobre os tipos primitivos das variáveis e dissecando uma que no caso vendo o que continha dentro

# Declarando variáveis
escreva = input("Digite alguma coisa: ")

# Imprimindo saídas de acordo com o desejado.
print("O tipo de da variável escreva é: ", type(escreva))

print('A variável "escreva" contém apenas letras: ', escreva.isalpha())
print('A variável "escreva" contém  letras maúsculas: ' , escreva.isupper())
print('A variável "escreva" contém letras minúsculas: ' , escreva.islower())
print('A variável "escreva" está capitalizada: ' , escreva.istitle())
print('A variável "escreva" contém só números: ' , escreva.isnumeric())
print('A variável "escreva" contém letras e números(alfanumérico): ' , escreva.isalnum())
print('A variável "escreva" contém decimal: ' , escreva.isdecimal())
print('A variável "escreva" contém apenas espaços: ' , escreva.isspace())


           
