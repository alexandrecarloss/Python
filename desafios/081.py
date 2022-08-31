lista = []
res = ''
while res != 'N':
    lista.append(int(input('Digite um valor: ')))
    while True:
        res = input('Quer continuar? [S/N] ').upper().strip()[0]
        if res in 'NS':
            break
lista.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')