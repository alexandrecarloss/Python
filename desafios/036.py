print('Empréstimo bancário')
valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

parc = valor / (anos * 12)
if parc > (sal * 0.3):
    print('Infelizmente não podemos conceder o empréstimo')
else:
    print(f'O valor das parcelas será de R${parc:.2f}')