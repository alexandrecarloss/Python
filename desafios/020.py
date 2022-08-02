import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A ordem de apresentção será: \nPrimeiro: {lista[0]} \nSegundo: {lista[1]} \nTerceiro: {lista[2]} \nQuarto: {lista[3]}')