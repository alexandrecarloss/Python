from random import randint
vitorias = 0
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
while True:
    c = randint(1, 10)
    j = int(input('Diga um valor: '))
    escolha = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    r = j + c
    print(f'Você jogou {j} e o computador jogou {c} total de {r} DEU ', end='')
    if r % 2 == 0:
        print(' PAR')
        if escolha == 'P':
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            break
    else:
        print(' ÍMPAR')
        if escolha == 'I':
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            break
print(f'GAME OVER! Você venceu {vitorias} vezes.')