from time import sleep
def maior(* núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for v in núm:
        print(v, end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 9)
maior(1, 2)
maior(6)
maior()
