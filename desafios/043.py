print('Índice de Massa Cospórea (IMC)')
peso = float(input('Informe seu peso '))
altura = float(input('Informe sua altura '))
imc = round(peso / pow(altura, 2), 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
print(imc)