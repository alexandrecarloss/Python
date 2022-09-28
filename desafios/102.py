def fatorial(n,show = False):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número pode ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    print('-' * 30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True and c > 1:
            print(f'{c} x', end=' ')
        if show == True and c == 1:
            print(f'{c} = ',end='')
    print(f)
    

fatorial(5, show=True)