from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = []
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'A {k} tirou {v} no dado')
    sleep(0.5)
print('Ranking dos jogadores: ')
print('-=' * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'O {i+1}° lugar: {v[0]} com {v[1]}')
# c = 1
# for i in sorted(jogo, key = jogo.get, reverse=True):
#     print(f'{c}° lugar: {i} com {jogo[i]}')
#     sleep(0.5)
#     c += 1


