numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ',end='')
    print(f'Você digitou o número {numero[n]}')
    while True:
        res = input('Você quer continuar [S/N] ').upper().strip()[0]
        if res in 'NS':
            break
    if res == 'N':
        break
