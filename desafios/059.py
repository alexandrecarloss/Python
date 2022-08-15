from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = 0
produto = 0
maior = n1
opção = 0

while opção !=5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>Qual é a sua opção? '))  
    
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} = {produto}')
    elif opção == 3:
        if n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}.')
        else:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente.') 
    print('-=-' * 15)  
print('Fim do programa! Volte sempre!')

