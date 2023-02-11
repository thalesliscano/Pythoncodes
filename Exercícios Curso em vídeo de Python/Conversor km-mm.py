# Aqui vou fazer um conversor km até mm e oque o exercício pedia era de "m" para cm

# Declarando variáveis e convertendo-a para o tipo float 
km = float(input("Digite um valor: "))

# Resolvendo os problemas 
# Aqui para converter basta ir multiplicando por 10 o valor dado, e ir atribuindo esse valor multiplicado para outras variáveis, e repetindo.  
hm = km * 10
dam = hm * 10
m = dam * 10
dm = m * 10
cm = dm * 10
mm = cm * 10

mParaCm = m * 100 

# Imprimindo o reusltado no formado de saída desejado
print('Tendo {}km o convesor obteve os seguintes resultados convertidos:\nhm = {}hm\ndam = {}dam\nm = {}m\ndm = {}dm\ncm = {}cm\nmm = {}mm\nO valor de "m" para cm é: {}'.format(km, hm, dam, m, dm, cm, mm,mParaCm))

