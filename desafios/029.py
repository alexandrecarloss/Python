v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    multa = (v - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido de 80Km/h\nVocê você deve pagar uma multa no valor de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')