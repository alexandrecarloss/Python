lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('A', 'E', 'I', 'O', 'U')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos ',end='')
    teste = palavra 
    for c in teste:
        if c in vogais:
            print(c.lower(),end=' ')
    
           
    
        
        
