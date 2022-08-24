num = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor >= (num[len(num) - 1]):
        num.append(valor)
        print('Adicionado ao final da lista...')
    elif valor < num[0]:
        num.insert(0, valor)
        print('Adicionado na posição 0 da lista')
    else:
        for i, v in enumerate(num):
            if valor < v:
                print(f'Índice {i}')
                print(f'Valor {v}')
            if valor > v:
                print(f'Índice {i} maior')
                print(f'Valor {v} maior')
    