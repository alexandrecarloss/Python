import random
from time import sleep
aleatorio = random.randint(0, 5)#Sorteia um número de 0 a 5
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 você consegue adivinhar?')
print('-=-' * 20)
n= int(input('Em que número eu pensei? '))#Pergunta o número do jogador
print('PROCESSANDO...')
sleep(2)
if n == aleatorio:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print(f'GANHEI! Eu pensei no número {aleatorio} e não no {n}.')