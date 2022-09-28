def notas(*n, sit=False):
    '''
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :paran sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    print('-' * 30)
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 5:
            r['Situação'] = 'Ruim'
        elif r['média'] < 7:
            r['Situação'] = 'Razoável'
        else:
             r['Situação'] = 'Boa'
    return r


#Programa principal
resp = notas(0.5, 5, 0, 6.5, 9, sit=True)
print(resp)
help(notas)

