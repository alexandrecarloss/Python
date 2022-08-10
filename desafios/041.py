import datetime
nas = int(input('Informe seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - nas
if idade < 9:
    cat = 'Mirim'
elif 9 < idade <= 14:
    cat = 'Infantil'
elif 14 < idade <= 19:
    cat = 'Junior'
elif 19 < idade <= 20:
    cat = 'Sênior'
else:
    cat = 'Master'
print(cat)