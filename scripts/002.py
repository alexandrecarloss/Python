from random import randint
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'{"JOGO DA VELHA":^30}')
maquina = randint(1, 9)
j = []
m = []
while True:
    # Exibe matriz
    print('-=' * 30)
    for l in range(0, 3):
        for c in range(0, 3):  
            print(f'[{matriz[l][c]:^5}]',end='')
        print()
    print('-=' * 30)
    # Jogada 1 jogador
    jogador = int(input('Escolha um número para jogar X: ')) 
    j.append(jogador)
    for l in range(0, 3):
        for c in range(0, 3):
            if  jogador == matriz[l][c]:
                matriz[l][c] = 'X'
    # Jogada 2 máquina
    while True:
        if maquina not in j and maquina not in m:
            m.append(maquina)
            for l in range(0, 3):
                for c in range(0, 3):
                    if maquina == matriz[l][c]:
                        print(f'Jogada em {matriz[l][c]}')
                        matriz[l][c] = 'O'             
            break 
        else:
            maquina = randint(1, 9)
    # Condicionais de vitória
    # linhas
    if matriz[0] == ['X', 'X', 'X'] or matriz[1] == ['X', 'X', 'X'] or matriz[2] == ['X', 'X', 'X']:
        vitória = 'Jogador'
        break
    if matriz[0] == ['O', 'O', 'O'] or matriz[1] == ['O', 'O', 'O'] or matriz[2] == ['O', 'O', 'O']:
        vitória = 'Máquina'
        break
    # Colunas
    c1 = [matriz[0][0], matriz[1][0], matriz[2][0]]
    c2 = [matriz[0][1], matriz[1][1], matriz[2][1]]
    c3 = [matriz[0][2], matriz[1][2], matriz[2][2]]
    if c1 == ['X', 'X', 'X'] or c2 == ['X', 'X', 'X'] or c3 == ['X', 'X', 'X']:
        vitória = 'Jogador'
        break
    if c1 == ['O', 'O', 'O'] or c2 == ['O', 'O', 'O'] or c3 == ['O', 'O', 'O']:
        vitória = 'Máquina'
        break
    # Diagonais
    d1 = [matriz[0][0], matriz[1][1], matriz[2][2]]
    d2 = [matriz[0][2], matriz[1][1], matriz[2][0]]
    print(f'd1 {d1}')
    print(f'd2 {d2}')
    if d1 == ['X', 'X', 'X'] or d2 == ['X', 'X', 'X']:
        vitória = 'Jogador'
        break
    if d1 == ['O', 'O', 'O'] or d2 == ['O', 'O', 'O']:
        vitória = 'Máquina'
        break
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):  
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-=' * 30)
print(f'{vitória} vence') 

