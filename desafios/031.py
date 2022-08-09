d = int(input('Qual a distância da viagem em Km?'))
if d <= 200:
    p = d * 0.5
    print(f'O preço será de R${p:.2f}')
else:
    p = d * 0.45
    print(f'O preço será de R${p:.2f}')
