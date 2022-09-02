tudo = [[],[]]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        tudo[0].append(valor)
    else:
        tudo[1].append(valor)
tudo[0].sort()
tudo[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {tudo[0]}')
print(f'Os valores ímpares digitados foram: {tudo[1]}')
