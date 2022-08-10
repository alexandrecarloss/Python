print('Qual número é o maior')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
maior = n1
if n2 > n1:
    print(f'{n2} é maior!')
elif n2 == n1:
    print('Não existe valor maior os dois são iguais!')
else:
    print(f'{n1} é maior!')