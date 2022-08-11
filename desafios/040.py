n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {m:.1f}')
if m < 5:
    print(f'Aluno REPROVADO')
elif 7 > m >= 5:
    print(f'Aluno em RECUPERAÇÃO')
else:
    print(f'Aluno APROVADO')