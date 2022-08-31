expressão = str(input('Digite uma expressão: ')).strip()
abre = fecha = 0
for c in range(0, len(expressão)):
    if expressão[c] == '(':
        abre += 1
    if expressão[c] == ')':
        fecha += 1
if abre == fecha:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão está errada!')
print(abre)
print(fecha)