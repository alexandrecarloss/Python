num = (int(input('Digite um número: ')), 
int(input('Digite outro número: ')), 
int(input('Digite mais um número: ')), 
int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na {num.index(3) + 1}° posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os números pares digitados foram: ',end='')
for c in num:
    if c % 2 == 0:
        print(c,end=' ')
        


# noves = 0
# for c in range(0, 4):
#     n = int(input('Digite um número: '))
#     print(n)
#     números = (n)
#     if n == 9:
#         noves += 1
    

# print(números)