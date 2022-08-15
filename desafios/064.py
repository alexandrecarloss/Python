n = 0
s = 0
c = 0
while n!= 999:
    n = int(input('Digite um número [999 para parar] '))
    if n != 999:
        s += n 
        c += 1
print(f'Você digitou {c} números, e a soma entre eles foi: {s}.')
