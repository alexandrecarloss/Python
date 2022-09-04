matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = ter = maiseg = 0
for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))
        if matriz[x][y] % 2 == 0:
            pares += matriz[x][y]
        if y == 2:
            ter += matriz[x][y]
        if x == 1 and y == 0 or x == 1 and matriz[x][y] > maiseg:
            maiseg = matriz[x][y]
print('-='*30)
for x in range(0, 3):
    for y in range(0, 3):  
        print(f'[{matriz[x][y]:^5}]',end='')
    print()
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {ter}')
print(f'O maior valor da segunda coluna é: {maiseg}')