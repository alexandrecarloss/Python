from datetime import date

while True:
    ano = date.today().year 
    print(ano)   
    dados = {'nome': input('Nome: '),
    'idade': int(input('Ano de Nascimento: ')), 'ctps': int(input('Carteira de Trabalho (0 não tem):'))}
    if dados['ctps'] == 0:
        break
    else:
        dados['contratação'] = int(input('Ano de Contratação: '))
        dados['salário'] = int(input('Salário: R$'))
        dados['aposentadoria'] = dados['contratação'] + 30 - dados['idade']
        dados['idade'] = ano - dados['idade']
        break
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
