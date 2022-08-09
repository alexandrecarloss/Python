sal = float(input('Qual o salário atual? R$'))
if sal > 1250:
    novo = sal * 1.1
else:
    novo = sal * 1.15
print(f'O salário com aumento será de: R${novo:.2f}')