matriz = []
for x in range(1, 4):
    for y in range(1, 4):
        matriz.append(x*y)
    print(matriz)
    
for x in range(1, 4):
    for y in range(1, 4):
        print(matriz[x]-1)