s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número inteiro: '))
    if n % 2 == 0:
        s += n
        cont += 1
if cont == 1:
    print(f'O único número par informado é: {s}')
print(f'A soma dos {cont} números pares informados é: {s}')