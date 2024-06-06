par = impar = i = 0
r = 'S'
while r == 'S':
    i = int(input('Digite um número: '))
    if i %  2 == 0:
        par += 1
    else:
        impar += 1
    r = str(input('Continuar? [S/N] ')).upper()
print('Pares: ', par, 'Impares: ', impar)