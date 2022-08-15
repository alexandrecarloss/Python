print('=' * 30)
print('      GERADOR DE PA')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA '))
termo = p
cont = 1

while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += r
    cont += 1
print('FIM')
#f = p + 10 * r
#Laço do número informado até o décimo

# for c in range(p, f, r):
#     print(f'{p}', end=' → ')
#     p += r
