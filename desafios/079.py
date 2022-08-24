n = []
while True:
    número = int(input('Digite um valor: '))
    if número not in n:
        n.append(número)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        res = input('Quer continuar? [S/N] ').upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('-=' * 30)
n.sort()
print(f'Você digitou os valores: {n}')
    

