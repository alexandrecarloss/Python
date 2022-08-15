res = ''
s = 0
m = 0 
c = 0
while res != 'N':
    n = float(input('Digite um número '))
    res = input('Quer continuar? [S/N] ').upper().strip()[0]
    while res not in 'NnSs':
        print('Valor inválido! ', end='')
        res = input('Quer continuar? [S/N] ').upper().strip()[0]
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    s += n
    m = s / c
print(f'Você digitou {c} números e a média foi {m}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
