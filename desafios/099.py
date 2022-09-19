def maior(* n):
    lista = []
    for v in n:
        lista.append(v)
    if lista == []:
        lista.append(0)
    print('-=' * 30)
    print('Analizando os valores passados...')
    for v in lista:
        print(v, end=' ')
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 9)
maior(1, 2)
maior(6)
maior()
