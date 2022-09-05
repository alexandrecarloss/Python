from time import sleep
from random import randint
print('-' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  Sorteando {jogos} Jogos  -=-=-=')
j = []
l = []
for c in range(0, jogos):
    while len(l) < 6:
        n = (randint(1, 60))
        if n not in l:
            l.append(n)
    l.sort()
    j.append(l[:])
    l.clear()
    print(f'Jogo {c + 1}: {j[c]}')
    sleep(0.5) 
print(f'-='*5,' < BOA SORTE! > ', '-=' * 5)

        
