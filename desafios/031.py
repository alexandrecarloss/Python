d = int(input('Qual a distância da su viagem viagem?'))
print(f'Você está prestes a começar uma viagem de {d}Km')
p = d * 0.5 if d <= 200 else d * 0.45
print(f'E o preço será de R${p:.2f}')
'''if d <= 200:
    p = d * 0.5
    print(f'Você está prestes a começar uma viagem de {d}Km \nE o preço será de R${p:.2f}')
else:
    p = d * 0.45
    print(f'Você está prestes a começar uma viagem de {d}Km \nE o preço será de R${p:.2f}')'''
