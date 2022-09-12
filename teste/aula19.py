pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': 19}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
