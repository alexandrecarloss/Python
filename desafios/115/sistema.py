from lib.interface import *
from lib.arquivo import *
from time import sleep
# Apagar arquivos :
# import os
# os.remove('nome')
arq = 'cursoemvideo.txt'

# try:
#     ref_arquivo = open('cursoemvide.txt',"x")
#     ref_arquivo.close()
# except Exception as erro:
#     print(erro)
# else:
#     print('sim')


if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
