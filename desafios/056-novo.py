somaidade = 0
médiaidade = 0
maioridadehomem = 0
maisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}° Pessoa -----')
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip())
    somaidade += idade
    if p == 1 and sexo == 'Mm':
        maioridadehomem = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        maisvelho = nome 
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4

print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {maisvelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')