print('-' * 30)
print('           LOJA SUPER BARATÃO')
print('-' * 30)
q = total = maisdemil = 0
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    total += preço
    if q == 0 or preço < barato:
        barato = preço
        nomebarato = nome
    if preço > 1000:
        maisdemil += 1
    while True:
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
    q += 1
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {maisdemil} produtos custando mais de mil.')
print(f'O produto mais barato foi {nomebarato} que custou {barato:.2f}')