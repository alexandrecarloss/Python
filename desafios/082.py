lista = []
ímpares = []
pares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else: 
        ímpares.append(n)
    res = input('Quer continuar? [S/N]').upper().strip()[0]
    if res in 'Nn':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {ímpares}')