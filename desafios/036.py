print('Empréstimo bancário')
valor = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

parc = valor / (anos * 12)

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos  valor das parcelas será de R${parc:.2f}')

if parc > (sal * 0.3):
    print('Empréstimo NEGADO!')
else:
    print(f'Empréstimo pode ser concedido!')