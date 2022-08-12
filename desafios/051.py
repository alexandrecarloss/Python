print('10 primeiros termos de uma progressão aritmética (PA)')
p = int(input('Informe o primeiro termo da PA '))
r = int(input('Informe a razão da PA '))
# Descobrindo o décimo número da PA
f = p + 10 * r
#Laço do número informado até o décimo
print(f)
for c in range(p, f, r):
    print(p)
    p += r
    
