print('=' * 30)
print('      GERADOR DE PA')
print('=' * 30)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA '))
termo = p
cont = 1
x = 10
y = 1
while y != 0:
    while cont <= x:
        print(f'{termo}', end=' → ')
        termo += r
        cont += 1
    print('PAUSA')
    y = int(input('Quantos termos você quer mostrar mais? '))
    x += y
print(f'Progressão finalizada com {cont - 1} números mostrados.')
    
        
