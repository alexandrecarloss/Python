from time import sleep


while True:
    def ajuda(res):
        msgfuncao = f'  Acessando o comando {res}'
        print('\033[44m')
        print('~' * (len(msgfuncao) + 4))
        print(msgfuncao,flush=True)
        sleep(1)
        print('~' * (len(msgfuncao) + 4))
        print('\033[m')
        print('\033[7m')
        help(res)
        sleep(1)
        print('\033[m')
    msg = '  SISTEMA DE AJUDA PyHELP'  
    print('\033[42m')
    print('~' * (len(msg) + 4))
    print(msg)
    print('~' * (len(msg) + 4))
    print('\33[m')
    resp = str(input('Função ou Biblioteca > ')).strip()
    if resp.lower() == 'fim':
        break
    ajuda(resp)

