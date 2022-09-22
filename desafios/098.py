from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.1)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.1)
            cont -= p
        print('FIM!')
    # if f > i:
    #     for c in range(i, f+p, p):
    #         print(i,end=' ',flush=True)
    #         sleep(0.5)
    #         i += p
    # elif f < i:
    #     for c in range(i, f-p, -p):
    #         print(i, end=' ',flush=True)
    #         sleep(0.5)
    #         i -= p
    # print('FIM!')
    


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)


    