print('-'* 50)
print(f'{"LISTAGEM DE PREÇO":^50}',)
print('-'* 50)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 17.9, 'Estojo', 25, 'Transferidor', 4.2,
'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
for c in range(0, len(listagem)):   
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end=' ')
    else:
        print(f'R${listagem[c]:>7.2f}')
print('-'* 50)
