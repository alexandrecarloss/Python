def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NEGADO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))

print(voto(nasc))