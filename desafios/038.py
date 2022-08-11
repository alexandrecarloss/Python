print('Qual número é o maior')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
maior = n2
if n1 > n2:
    print(f'{n1} é maior!')
elif n1 == n2:
    print('Não existe valor maior os dois são IGUAIS!')
else:
    print(f'{n2} é maior!')