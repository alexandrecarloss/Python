from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Seu ano de nascimento: '))
    idade = atual - nasc
    print()
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} maiores de idade e {menor} menores de idade.')