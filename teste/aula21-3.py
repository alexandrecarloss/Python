# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')


# a = 5
# teste(a)
# print(f'A fora vale {a}')

# def somar(a=0, b=0, c=0):
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela
# #     :param a: o primeiro valor
# #     :param b: o segundo valor
# #     :param c: o terceiro valor
# #     :return: sem retorno
# #     Função criada por Gustavo Guanabara do canal curso em vídeo
#     """
#     s = a + b + c
#     return s
# r1 = somar(3, 2, 5)
# r2 = somar(8, 4)
# r3 = somar(4)
# print(f'Os resultados faram {r1}, {r2} e {r3}')

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
# # n = int(input('Digite um número: '))
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')