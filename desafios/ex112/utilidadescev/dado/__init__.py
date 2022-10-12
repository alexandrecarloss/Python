def leiaDinheiro(p):
    while True:
        p = input(p)
        if ',' in p:
            p = p.replace(',','.')
        if str(p).replace('.','',1).isdigit():
            p = float(p)
            return p           
        else:
            print(f'\033[31mERRO! {p} é um preço inválido\033[m')
            p = 'Digite o preço: R$'
        
    
