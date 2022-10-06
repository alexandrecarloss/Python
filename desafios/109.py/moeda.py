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
