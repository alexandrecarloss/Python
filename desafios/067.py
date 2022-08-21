while True:
    v = int(input('Quer ver a tabuada de qual valor? [Negativo para parar] '))
    if v < 0:
        break
    print('-'*30)
    for c in range(1, 11):
            print(f'{v} x {c} = {v * c}')
    print('-'*30)
print('Programa TABUADA encerrado. volte sempre!')