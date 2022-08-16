print('=' * 30)
print('           BANCO CEV')
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
ced50 = ced20 = ced10 = ced1 = 0
while True:
    ced50 = valor // 50
    valor = valor % 50
    if valor == 0:
        break
    ced20 = valor // 20
    valor = valor % 20
    if valor == 0:
        break
    ced10 = valor // 10
    valor = valor % 10
    if valor == 0:
        break
    ced1 = valor // 1
    valor = valor % ced1
    if valor == 0:
        break
print(f'Total de {ced50} cédulas de R$50.00')
print(f'Total de {ced20} cédulas de R$20.00')
print(f'Total de {ced10} cédulas de R$10.00')
print(f'Total de {ced1} cédulas de R$1.00')
print('=' * 30)
print('Volte sempre ao banco CEV tenha um bom dia!')