a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
#Solução Curso em Vídeo

'''#Verificando o menor
menor = a
if b < a and b < b:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor digitado foi {menor}')

#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado foi {maior}')'''

#Solução alternativa
n = [a, b, c]
print(f'O maior valor digitado foi {max(n)}')
print(f'O menor valor digitado foi {min(n)}')


#Minha primeira solução
'''# Se os números forem iguais
if n1 == n2 and n2 == n3:
    print('Os números são iguais')
else:
# Se o primeiro for maior ou um dos maiores
    if n1 >= n2 and n1 >= n3:
        if n1 == n2:
            print('O primeiro e o segundo são iguais e maiores que o terceiro!')
        if n1 == n3:
            print('O primeiro e o terceiro são iguais e maiores que o segundo!')
        if n1 > n2 and n1 > n3:
            print('O primeiro é maior!')
            if n2 == n3:
                print('E o segundo e terceiro são menores e iguais!')
            if n2 < n3:
                print('E o segundo é menor!')
            if n3 < n2:
                print('E o terceiro é menor!')
    else:
        # Se o segundo for maior ou um dos maiores
        if n2 >= n1 and n2 >= n3:
            if n2 == n3:
                print('O segundo e o terceiro são iguais e maiores que o primeiro!')
            if n2 > n1 and n2 > n3:
                print('O segundo é maior!')
                if n1 == n3:
                    print('E o primeiro e terceiro são menores e iguais!')
                if n1 < n3:
                    print('E o primeiro é menor!')
                if n3 < n1:
                    print('E o terceiro é menor!')
        else:
            # Se o terceiro for maior ou um dos maiores
            if n3 > n1 and n3 > n2:
                print('O terceiro é maior!')
                if n1 == n2:
                    print('E o primeiro e segundo são menores e iguais!')
                if n1 < n2:
                    print('E o primeiro é menor!')
                if n2 < n1:
                    print('E o segundo é menor!')'''

