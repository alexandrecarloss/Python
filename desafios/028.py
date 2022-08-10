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
import random
from time import sleep
aleatorio = random.randint(0, 5)#Sorteia um número de 0 a 5
print(f'{cores["azul"]}-=-' * 20)
print(f'{cores["limpa"]}Vou pensar em um número entre 0 e 5 você consegue adivinhar?')
print(f'{cores["vermelho"]}-=-' * 20)
n= int(input(f'{cores["limpa"]}Em que número eu pensei? '))#Pergunta o número do jogador
print('PROCESSANDO...')
sleep(2)
if n == aleatorio:
    print(f'{cores["verde"]}PARABÉNS!{cores["limpa"]} Você conseguiu me vencer! ')
else:
    print(f'{cores["vermelho"]}GANHEI!{cores["limpa"]} Eu pensei no número {cores["ciano"]}{aleatorio}{cores["limpa"]} e não no {cores["vermelho"]}{n}{cores["limpa"]}.')