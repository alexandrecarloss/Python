#Definir média 0
m = 0
#laço de 0 a 4 pede nome sexo e idade
for c in range(0, 4):
    nome = input('Digite seu nome: ')
    sexo = input('Sexo (M) ou (F): ').upper()
    #Testar se o sexo é M ou F
    # if sexo != 'M' and sexo != 'F':
    #     print(sexo)
    #     print('Letra inválida. Por favor informe (M) ou (F).')
    #     sexo = input('Sexo (M) ou (F): ').upper()
    idade = int(input('Informe sua idade: '))
    #no primeiro laço mulheres menores = 0 e velho = idade
    if c == 0:
        mmenor = 0
        velho = idade
    # Se o primeiro laço for homem hvelho = velho e maisevelho = nome
    if c == 0 and sexo == 'M':
        hvelho = velho
        maisvelho = nome
    # Se o sexo for M e idade maior que hvelho hvelho = idade e maisvelho = nome
    if sexo == 'M' and idade > hvelho:
        hvelho = idade
        maisvelho = nome
    # Se sexo for F e idade < 20 mulheres menores += 1
    if sexo == 'F' and idade < 20:
        mmenor += 1
    #média recebe média mais idade
    m += idade 
m = m / 4
print(c)

print(f'A média de idade do grupo é de {m}.')
print(f'O homem mais velho tem {hvelho} anos. E se chama {maisvelho}')    
print(f'Existem {mmenor} mulheres com menos de 20 anos no grupo.')