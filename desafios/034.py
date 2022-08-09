sal = float(input('Qual o salário atual? R$'))
if sal > 1250:
    novo = sal * 1.1
else:
    novo = sal * 1.15
print(f'Para quem ganhava R${sal:.2f} o salário com aumento será de R${novo:.2f}')