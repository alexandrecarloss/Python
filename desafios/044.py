preco = float(input('Informe o preço do produto R$'))
pag = float(input('De que maneira você que pagar? \n 1 para à vista no dinheiro ou no cheque com desconto de 10% \n 2 para pagar à vista no cartão com 5% de desconto \n 3 para pagar no cartão em até duas vezes com preço normal \n 4 para pagar no cartão em 3 vezes ou mais com juros de 20% \n'))

if pag == 1:
    valor = preco * 0.9
elif pag == 2:
    valor = preco * 0.95
elif pag == 3:
    valor = preco
elif pag == 4:
    valor = preco * 1.2
print(f'O valor a ser pago é: R${valor:.2f}')