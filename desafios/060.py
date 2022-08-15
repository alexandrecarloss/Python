# n = int(input('Digite um número para calcular seu fatorial: '))
# c = n
# f = 1
# print(f'Calculando {n}!')
# while c > 0:
#     print(f'{c}',end='')
#     print(f' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print(f' {f}')

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}!')
for c in range(c, 0, -1):
    print(c, end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}')