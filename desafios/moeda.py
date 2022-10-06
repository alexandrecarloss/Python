def metade(p):
    p *= 0.5
    return round(p, 2) 


def dobro(p):
    p *= 2
    return round(p, 2) 

def aumentar(p, t):
    p *= 1 +(t / 100)
    return round(p, 2) 

def diminuir(p, t):
    p *= 1 - (t / 100)
    return round(p, 2) 

def moeda(t):
    round(t, 2)
    x = str(t).replace('.',',')
    list(x)
    x = 'R$' + x
    

    
    
    return x
