alunos = []
notas = []
while True:
    aluno = []
    nome = input('Nome: ').strip()
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(nome)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()
    res = input('Quer continuar? [S/N] ').strip()[0]
    if res in'Nn':
        break
print('-=' * 30)
print(f'{"N°":<5} {"NOME":<10} {"MÉDIA":>5}')
print('-' * 30)
# #Todos
# print(alunos)
# #primeiro
# print(alunos[0])
# #nome primeiro
# print(alunos[0][0])
# #notas primeiro
# print(alunos[0][1])
# #primeira nota primeiro
# print(alunos[0][1][0])
# #segunda nota primeiro
# print(alunos[0][1][1])
for c in range(0, len(alunos)):
    m = ((alunos[c][1][0]) + (alunos[c][1][1]))
    print(f'{c:<5} {alunos[c][0]:<10} {m:>5}')
while True:
    print('-'*40)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    else:
        print(f'As notas de {alunos[n][0]} são: {alunos[n][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')


