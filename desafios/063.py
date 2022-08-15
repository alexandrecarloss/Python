print('-' * 30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print(f'{t1} → {t2}',end='')
c = 3
while c <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f' → {t3}',end='')
    c += 1
print(' → FIM')

# f = 0
# c = n
# atual = 0
# anterior = 0
# print('~'*15)
# while c > 0: 
#     print(f,end=' ')
 
#     if c > (n - 3): #tempo 1 2 3 4
#         anterior = 1
#     else:
#         anterior = atual
#     if c  <= (n - 2): #tempo 3 em diante
#         atual = f
#     f = atual + anterior 
#     c -= 1



