from random import randint
print('Sou seu computador...')
computador = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual é o seu palpite? '))
quantidade = 1
while jogador != computador:
    if jogador > computador:
        print('Menos...')
    if jogador< computador:
        print('Mais')
    jogador = int(input('Tente mais uma vez.'))
    quantidade += 1
print(f'Acertou com {quantidade} tentativas. Parabéns!')