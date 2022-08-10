nome = str(input('Qual é o seu nome? '))
if nome == 'Carlos':
    print(f'Belo nome meu parceiro')
elif nome == '':
    print('Nome não informado')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil')
elif nome == 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Nome bem normal')
print(f'Tenha um bom dia {nome}')