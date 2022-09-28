def leiaInt(msg):
    print('-' * 30)
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            n = int(n)
            ok = True
        else:
            print('\033[31m ERRO! Digite um número inteiro válido \033[m')
        if ok:
            break
    return valor
        

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
