from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados')
for k, v in jogo.items():
    print(f'A {k} tirou {v} no dado')
    sleep(1)
print('  == Ranking dos jogadores ==')
print('-=' * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

# Forma que eu fiz
# c = 1
# for i in sorted(jogo, key = jogo.get, reverse=True):
#     print(f'{c}° lugar: {i} com {jogo[i]}')
#     sleep(0.5)
#     c += 1


