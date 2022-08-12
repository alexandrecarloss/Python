# Pedir a frase e tirar espaços dos lados
frase = input('Escreva uma frase: ').strip()
#Separar a frase
separado = frase.split()
#Juntar sem espaço
semesp = ''.join(separado)
#Declara a variável tamanho com o valor do sem espaço
tamanho = len(semesp) - 1

print(f'A frase {semesp}')
x = tamanho
y = 0
# Solução sem for
# reverso = semesp[tamanho::-1]
# if reverso == semesp:
#     print('É palíndromo!')
reverso = semesp
a = tamanho
for c in range(tamanho,-1,-1):
    if reverso[y] == semesp[c]:
        a -= 1
    x -= 1
    y += 1
if a == -1:
    res = 'É palíndroma'
else:
     res = 'Não é palíndroma'
print(f'{res}')



# reverso = (frase[[len(frase)]::-1])
# if frase == reverso:
#     print('Simm')
# print(len(frase))