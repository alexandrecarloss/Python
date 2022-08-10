n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Aluno REPROVADO')
elif 5 <= m and m <= 6.9:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO')