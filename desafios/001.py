cores = {'limpa':'\033[m',
'azul':'\033[34m',
'bmagenta':'\033[45m',
'bbranco':'\033[107m'
}


nome = input (f'{cores["bmagenta"]}Qual é o seu nome? {cores["limpa"]}')
print (f'Olá, {cores["azul"]}{nome}{cores["limpa"]}, prazer em te conhecer!')
    
