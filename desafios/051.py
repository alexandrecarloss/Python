print('=' * 30)
print('      10 TERMOS DE UMA PA')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Informe a razão da PA '))
f = p + 10 * r
#Laço do número informado até o décimo

for c in range(p, f, r):
    print(f'{p}', end=' → ')
    p += r
print('Acabou')
