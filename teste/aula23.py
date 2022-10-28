# primt(x) sintaxe
# print(x) semântica
# n = int(input('Digite um número: '))
# print(f'Você digitou o número {n}')
# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')
# r = 2 / '2'
# lst = [3,5,4]
# print(lst[3])
# from moeda import uteis 


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Infelizmente tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro: 
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')