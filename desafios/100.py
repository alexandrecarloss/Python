from random import randint
números = []
def sorteio():
    números.clear()
    for c in range(0, 5):
        números.append(randint(1, 10))
    print('Sorteando 5 valores da lista: ',end='')
    for v in números:
        print(v, end=' ')
    print('PRONTO!')
def somaPar():
    soma = 0
    for v in números:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {números}, temos {soma}')
sorteio()
somaPar()
