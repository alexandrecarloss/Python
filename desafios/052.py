n = int(input('Digite um número: '))
#Declara variável
x = 0
#Laço iniciando de número informado até 1 passo -1
for c in range(n, 0, -1):
    #Condição para se o resto da divisão por dois for 0
    if n % c == 0:
        #Variável é somada mais um se sim
        x += 1
#Verifica se a variável for  divisível por 2 (um e por ele mesmo).
if x == 2:
    print('É primo!')
    

        