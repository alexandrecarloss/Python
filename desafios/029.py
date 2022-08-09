v = float(input('Velocidade em Km/h: '))
if v > 80:
    multa = (v - 80) * 7
    print(f'Você foi multado no valor de R${multa}!')