# def título(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)


# título('   CURSO EM VÍDEO')
# título('Oi')

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print('A soma A + B vale: ')
#     print(s)


# soma(b=4, a=5)
# soma(7, 2)
# soma(3, 9)

# def contador(* núm):   
#     tam = len(núm)
#     print(f'Recebi os valores {núm} e são ao todo {tam} números')
    


# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst):
#     pos = 0 
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1


# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somaando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)