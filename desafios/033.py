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
a = float(input(f'{cores["amarelo"]}Digite o primeiro número: '))
b = float(input(f'{cores["azul"]}Digite o segundo número: '))
c = float(input(f'{cores["verde"]}Digite o terceiro número: '))
#Solução Curso em Vídeo

'''#Verificando o menor
menor = a
if b < a and b < b:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')

#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}')'''

#Solução alternativa
n = [a, b, c]
print(f'{cores["limpa"]}O maior valor digitado foi {cores["ciano"]}{max(n)}{cores["limpa"]}')
print(f'O menor valor digitado foi {cores["vermelho"]}{min(n)}{cores["limpa"]}')


#Minha primeira solução
'''# Se os números forem iguais
if n1 == n2 and n2 == n3:
    print('Os números são iguais')
else:
# Se o primeiro for maior ou um dos maiores
    if n1 >= n2 and n1 >= n3:
        if n1 == n2:
            print('O primeiro e o segundo são iguais e maiores que o terceiro!')
        if n1 == n3:
            print('O primeiro e o terceiro são iguais e maiores que o segundo!')
        if n1 > n2 and n1 > n3:
            print('O primeiro é maior!')
            if n2 == n3:
                print('E o segundo e terceiro são menores e iguais!')
            if n2 < n3:
                print('E o segundo é menor!')
            if n3 < n2:
                print('E o terceiro é menor!')
    else:
        # Se o segundo for maior ou um dos maiores
        if n2 >= n1 and n2 >= n3:
            if n2 == n3:
                print('O segundo e o terceiro são iguais e maiores que o primeiro!')
            if n2 > n1 and n2 > n3:
                print('O segundo é maior!')
                if n1 == n3:
                    print('E o primeiro e terceiro são menores e iguais!')
                if n1 < n3:
                    print('E o primeiro é menor!')
                if n3 < n1:
                    print('E o terceiro é menor!')
        else:
            # Se o terceiro for maior ou um dos maiores
            if n3 > n1 and n3 > n2:
                print('O terceiro é maior!')
                if n1 == n2:
                    print('E o primeiro e segundo são menores e iguais!')
                if n1 < n2:
                    print('E o primeiro é menor!')
                if n2 < n1:
                    print('E o segundo é menor!')'''

