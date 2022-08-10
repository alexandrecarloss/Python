print('-=-' * 20)
print('Analisando triângulo')
print('-=-' * 20)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('\033[42mPodem\033[m formar um triângulo')
else:
    print('\033[41mNão podem\033[m formar um triângulo')