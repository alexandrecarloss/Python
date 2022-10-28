while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
    except (ValueError, TypeError):
        print('\033[31mERRO: por favor digite um número inteiro válido!\033[m')
    except KeyboardInterrupt:
        print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        inteiro = 0
        break
    except Exception as erro:
        print(f'\033[31mO erro encontrado foi {erro.__cause__}\033[m')
    else:
        break 
while True:
    try:
        real = float(input('Digite um número real: '))
    except (ValueError, TypeError):
        print('\033[31mERRO: por favor digite um número real válido!\033[m')
    except KeyboardInterrupt:
        print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        real = 0
        break
    except Exception as erro:
        print(f'\033[31mO erro encontrado foi {erro.__cause__}\033[m')
    else:
        break 

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')