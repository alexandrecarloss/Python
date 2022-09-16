m = 0
pessoa = {}
grupo = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).strip()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    while True:
        res = str(input('Quer continuar [S/N] '))
        if res not in 'SsNn':
            print('ERRO! Responda apenas com S ou N')
        else:
            break
    grupo.append(pessoa.copy())
    if res in 'Nn':
                break
print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
for c in range(0, len(grupo)):
    m += grupo[c]['idade']
m = m / len(grupo)
print(f'B) A média de idade é de {m:.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for c in range(0, len(grupo)):
    if grupo[c]['sexo'] in 'Ff':
        print(grupo[c]['nome'], end=' ')
print()
print(f'Lista das pessoas que estão acima da média: ',end='')
for c in range(0, len(grupo)):
    if grupo[c]['idade'] > m:
        print(grupo[c])