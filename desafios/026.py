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
from unidecode import unidecode

frase = unidecode(str(input('Digite uma frase: '))).strip()
print(f'A letra {cores["azul sublinhado"]}A{cores["limpa"]} aparece {(frase.upper().count("A"))} vezes na frase.')
print(f'A primeira letra {cores["azul sublinhado"]}A{cores["limpa"]} apareceu na posição: {frase.upper().find("A") + 1}.')
print(f'A última letra {cores["azul sublinhado"]}A{cores["limpa"]} apareceu na posição: {frase.upper().rfind("A") + 1}')
