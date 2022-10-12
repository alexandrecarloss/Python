def metade(p, x=False):
    p *= 0.5
    p = round(p, 2)
    if x == True:
        valor = str(p).replace('.',',')
        valor = 'R$' + valor
        return valor
    else:
        return p 


def dobro(p, x=False):
    p *= 2
    p = round(p, 2)
    if x == True:
        valor = str(p).replace('.',',')
        valor = 'R$' + valor
        return valor
    else:
        return p 

def aumentar(p, t, x=False):
    p *= 1 +(t / 100)
    p = round(p, 2)
    if x == True:
        valor = str(p).replace('.',',')
        valor = 'R$' + valor
        return valor
    else:
        return p  

def diminuir(p, t, x=False):
    p *= 1 - (t / 100)
    p = round(p, 2)
    if x == True:
        valor = str(p).replace('.',',')
        valor = 'R$' + valor
        return valor
    else:
        return p 

def moeda(t):
    round(t, 2)
    x = str(t).replace('.',',')
    x = 'R$' + x    
    return x


def resumo(p, a, r):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analizado: ":<20} {moeda(p)}')
    print(f'{"Dobro do preço: ":<20} {dobro(p, True)}')
    print(f'{"Metade do preço: ":<20} {metade(p, True)}')
    print(f'{a}%{" de aumento: ":<17} {aumentar(p, a, True)}')
    print(f'{r}%{" de redução: ":<17} {diminuir(p, r, True)}')
    print('-' * 30)