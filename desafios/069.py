print('-'* 30)
print('     CADASTRE UMA PESSOA')
print('-'* 30)
res = ''
mais18 = homens = mulher20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    while True:
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulher20 += 1
        if sexo in 'MF':
            break
    print('-'* 30)
    while True:
        res = input('Quer continuar? [S/N] ').upper().strip()[0]
        if res in 'SN':
            break
    if res == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')
    
    
    