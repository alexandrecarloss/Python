def notas(*n, sit=False):
    '''
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :paran sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    print('-' * 30)
    aluno = {}
    aluno['total'] = aluno['maior'] = aluno['menor'] = aluno['média'] = s = 0
    for i, v in enumerate(n):
        if v != True:
            aluno['total'] += 1
            s += v
            aluno['média'] = s / aluno['total']
            if i == 0 or v < aluno['menor']:
                aluno['menor'] = v
            if i == 0 or v > aluno['maior']:
                aluno['maior'] = v
    if sit == True:
        if aluno['média'] < 5:
            aluno['Situação'] = 'Ruim'
        elif aluno['média'] < 7:
            aluno['Situação'] = 'Razoável'
        else:
             aluno['Situação'] = 'Boa'
    resp = aluno
    return resp

    
resp = notas(6.5, 5, 10, 6.5, 9,False)
print(resp)

