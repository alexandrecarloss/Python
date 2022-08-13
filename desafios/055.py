print('Mais e menos pesado')



# Laço de 0 a 4 para adicionar y no array x de posição c somando y += 1
# for c in range(0, 5):
#     x.insert(c, y)
#     y += 1

# Solução com min e max
# for c in range(0, 5):
#     peso = float(input('Informe seu peso: '))
#     x.insert(c, peso)
#     menor = min(x)
#     maior = max(x)

#Laçoo c de 1 a 6 pede o peso
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    #O maior e menor recebe o primeiro termo do array
    if c == 1:
        menor = peso
        maior = peso
    #Se o peso for maior que maior então maior recebe peso
    if peso > maior:
        maior = peso
    # Se o peso for menor que o menor então menor recebe peso
    if peso < menor:
        menor = peso
print(f'O menor peso informado foi de {menor}Kg')
print(f'O maior peso informado foi de {maior}Kg')


