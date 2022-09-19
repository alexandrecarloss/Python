def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f > i and p > 0:
        for c in range(i, f+p, p):
            print(i,end=' ')
            i += p
    elif f < i and p > 0:
        for c in range(i, f-p, -p):
            print(i, end=' ')
            i -= p
    print('FIM!')
    print('-=' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)


    