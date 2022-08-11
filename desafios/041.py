import datetime
nas = int(input('Ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - nas
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    cat = 'Mirim'
elif 9 < idade <= 14:
    cat = 'Infantil'
elif idade <= 19:
    cat = 'Junior'
elif idade <= 25:
    cat = 'Sênior'
else:
    cat = 'Master'
print(cat)