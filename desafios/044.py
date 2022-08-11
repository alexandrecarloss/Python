print('{:=^40}'.format(' LOJAS ALEXANDRE '))
preco = float(input('Preço da compra R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    valor = preco * 0.9
elif opção == 2:
    valor = preco * 0.95
elif opção == 3:
    valor = preco
    parcela = preco / 2
    print(f'Sua compra sera parcelada em 2x de R${parcela:.2f} SEM JUROS.')
elif opção == 4:
    valor = preco * 1.2
    totparc = int(input('Quantas parcelas? '))
    parcela = preco / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    valor = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')