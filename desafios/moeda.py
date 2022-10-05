def metade(p):
    p *= 0.5
    return p


def dobro(p):
    p *= 2
    return p

def aumentar(p, t):
    p *= 1 +(t / 100)
    return p

def diminuir(p, t):
    p *= 1 - (t / 100)
    return p
def moeda(t):
    str(t.replace('.',','))
    x = (f'R${t:.2f}')
    
    return x
