from time import sleep
c = ('\033[m', # 0 - sem cor
    '\033[41m', # 1 - vermelho
    '\033[42m', # 2 - verde
    '\033[43m', # 3 - amarelo
    '\033[44m', # 4 - azul
    '\033[45m', # 5 - roxo
    '\033[47m', # 6 - ciano
    '\033[7m', # 7 - branco
    )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6])
    help(com)
    print(c[0])
    sleep(1.5)

def título(msg, cor=0):
    tam = len(msg)
    print(c[cor])
    print('~' * (tam + 4))
    print(f'  {msg}')
    print('~' * (tam + 4))
    print(c[0])
    sleep(1)
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)