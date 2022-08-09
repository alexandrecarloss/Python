import random
aleatorio = random.randint(0, 5)
n= int(input('Qual número entre 0 e 5 você acha que é o escolhido? '))
if n == aleatorio:
    print('Você venceu! ')
else:
    print(f'O número escolhido foi {aleatorio} você perdeu.')