from random import randint
aleatorio = randint(1, 3)
pessoa = int(input('Qual número: '))
if aleatorio == pessoa:
    print('Você venceu!')
else:
    print('Que pena o número era ', aleatorio)