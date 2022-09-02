lista = []
l2 = []
res = 'S'
while res not in 'Nn':
    lista.append(input('Nome: ' ))
    lista.append(float(input('Peso: ')))
    res = input('Quer continuar? [S/N] ').upper().strip()[0]
    l2.append(lista[:])
    lista.clear()   
print(l2)
print('-='*30)
print(f'Ao todo você cadastrou {len(l2)} pessoas')
nomem = []
nomep = []
for c in range(0, len(l2)):
    if c == 0 or (l2[c][1]) >= maior:
        maior = l2[c][1]
for c in range(0, len(l2)):
    if l2[c][1] == maior:
        nomem.append(l2[c][0])
for c in range(0, len(l2)):
    if c == 0 or (l2[c][1]) <= menor:
        menor = l2[c][1]
for c in range(0, len(l2)):
    if l2[c][1] == menor:
        nomep.append(l2[c][0])
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {nomem}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {nomep}')



