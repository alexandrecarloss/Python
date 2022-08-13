#Pede a frase elimina os espaços dos lados e transforma em maiúsculas
frase = str(input('Digite uma frase: ')).strip().upper()
#separa a frase em palavras
palavras = frase.split()
#junta as palavras
junto = ''.join(palavras)
#declara o inverso vazio
inverso = ''
#O inverso da palavra com manipulação de string
inverso = junto[::-1]
#laço de tamanho do junto -1 até 0 voltando -1
'''for letra in range(len(junto) - 1, -1, -1):
    #inverso recebe inverso mais letra na posição letra
    inverso += junto[letra]'''
print(f'O inverso de {junto} é: {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

