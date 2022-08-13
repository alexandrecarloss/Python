cores = {    #cores normais

         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[97m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;97;m',

                #cores em negrito

         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;97',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',

               #cores sublinhadas

         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;97m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'
         }
fundo = {
    'vermelho':'\033[41m',
    'verde':'\033[42m',
    'amarelo':'\033[43m',
    'azul':'\033[44m',
    'magenta':'\033[45m',
    'ciano':'\033[46m'
}
#Pede o número
n = int(input('Digite um número: '))
#Declara variável de controle
x = 0
#Laço iniciando de 1 até número informado em passo 1
for c in range(1, n + 1):
    #Variável cor recebe vermelho para os que não são divisíveis pelo contador
    cor = "vermelho"
    #Condição para se o resto da divisão poelo contador for 0
    if n % c == 0:
        #Variável de controle é somada mais um se sim e cor = amarelo
        x += 1
        cor = "amarelo"
    #Escreve o número em ordem crescente com a cor da variável cor
    print(f'{cores[cor]}{c}{cores["limpa"]}',end=' ')

print(f'O número {n} foi divisível {x} vezes e por isso ele', end=' ')
#Verifica se a variável for primo / divisível por 2 (um e por ele mesmo).
if x == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
    

        