#Declaração de listas
valores = list()
posmai = []
posmen = []
# Receber 5 valores em valores
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
#verificar o menor e maior de valores
for c, v in enumerate(valores):
    if c == 0:
        menor = maior = v
    if v > maior:
        maior = v
    if v < menor:
        menor = v
# Verificar a posição dos maiores e menores
for c, v in enumerate(valores):
    if v == maior:
        posmai.append(c)
    if v == menor:
        posmen.append(c)
#Print dos valores 
print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}  nas posições ',end='')
for c in range(0, len(posmai)):
    print(f'{posmai[c]}...', end='')
print(f'\nO menor valor digitado foi {menor}  nas posições ',end=' ')
for c in range(0, len(posmen)):
    print(f'{posmen[c]}...',end=' ')
