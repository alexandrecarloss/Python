d = int(input('Quantos dias alugados? '))
km = float(input('Qauntos quilômetros rodados? '))
a = (d * 60) + (km * 0.15)
print(f'O valor a pagar é de R${a:.2f}')