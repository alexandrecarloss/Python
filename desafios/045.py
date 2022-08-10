import random
print("=-=" * 20)
print('JOKENPÔ!')
mac = random.randint(1, 3)
j = input('Qual você escolhe pedra(1), papel(2) ou tesoura(3)? ')


if j == '1':
    j = 'pedra'
if j == '2':
    j = 'papel'
if j == '3':
    j = 'tesoura'
print(j)
if mac == 1:
    c = 'pedra'
elif mac == 2:
    c = 'papel'
else: 
    c = 'tesoura'

if c == j:
    print('EMPATE')
elif c == 'pedra' and j == 'tesoura':
    print('TESOURA PERDEU')
elif c == 'papel' and j == 'pedra':
    print('PEDRA PERDEU')
elif c == 'tesoura' and j == 'papel':
    print('PAPEL PERDEU')

elif j == 'pedra' and c == 'tesoura':
    print('VOCÊ VENCEU')
elif j == 'papel' and c == 'pedra':
    print('VOCÊ VENCEU')
elif j == 'tesoura' and c == 'papel':
    print('VOCÊ VENCEU')

print(c)