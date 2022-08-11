from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print('-=' * 11)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: # computador jogou pedra
    if jogador == 0: # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1: #jogador jogou papel
        print('JOGADOR VENCE')
    elif jogador == 2: #jogador jogou tesoura
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 0: # jogador jogou pedra
        print('COMPUTADOR VENCE')
    elif jogador == 1: #jogador jogou papel
        print('EMPATE')
    elif jogador == 2: #jogador jogou tesoura
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0: # jogador jogou pedra
        print('JOGADOR VENCE')
    elif jogador == 1: #jogador jogou papel
        print('COMPUTADOR VENCE')
    elif jogador == 2: #jogador jogou tesoura
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')