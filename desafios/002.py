cores = {'limpa':'\033[m',
'azul':'\033[33m',
'vermelho':'\033[31m',
'verde':'\033[32m',
'bciano':'\033[46m'}


dia = input (f'{cores["azul"]}Dia = {cores["limpa"]}')
mes = input (f'{cores["vermelho"]}Mês = {cores["limpa"]}')
ano = input (f'{cores["verde"]}Ano = {cores["limpa"]}')
print (f'{cores["bciano"]}Você nasceu no dia {dia} de {mes} de {ano} correto?{cores["limpa"]}')
