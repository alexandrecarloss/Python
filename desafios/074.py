from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),randint(0, 10))
print(f'Os valores sorteados foram: ',end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')






# from random import randint
# numeros = []
# for c in range(0, 5):
#     n = randint(0, 10)
#     if c == 0 or n > maior:
#         maior = n
#     if c == 0 or n < menor:
#         menor = n
#     numeros.append(n)
#     c += 1
# print(f'Os valores sorteados foram: ',end='')
# for x in range(0, len(numeros)):
#     print(f'{numeros[x]} ',end='')   
# print('')
# print(f'O maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')
