import datetime

print('-'*10,'Alistamento','-'*10)
#Pedir a data de nascimento
dianasc = datetime.date.today().day
mesnasc = datetime.date.today().month
anonasc = int(input('Digite o seu ano de nascimento: '))

#Verificar o ano atual
atual = datetime.date.today().year

#Verificando a diferença entre o ano atual e o ano de nascimento
ano = atual - anonasc

'''
#Resolução normal
if ano == 18:
    print('Ano do alistamento.')
elif ano == 17:
    print('Falta 1 ano para o alistamento.')
elif ano < 18:
    print(f'Faltam {(ano - 18) * -1} anos para o alistamento.')
elif ano == 19:
    print('Já se passou um ano do alistamento.')
else:
    print(f'Já se passaram {ano - 18} do alistamento.')
'''

if ano == 17 or ano == 18 or ano == 19:
    a = 'ano'
else:
    a = 'anos'
print(f'Para quem nasceu em {anonasc} tem {ano} anos.')
#Dia do alistamento
if ano == 18 and mesnasc == 1 and dianasc == 1:
    print(f'Dia do alistamento.')
#Antes do alistamento
elif ano == 17 and mesnasc == 1 and dianasc == 1:
    print(f'Falta {(ano - 18) * -1} {a} para o alistamento.')
elif ano < 18:
    print(f'Faltam {(ano - 17) * -1} anos {(mesnasc - 11) * -1} meses e {(dianasc - 30) * -1} dias para o alistamento.')
elif ano == 19 and dianasc == 1 and mesnasc == 12:
    print(f'Já se passou 1 ano do alistamento.')
#Depois do alistamento
else:
    print(f'Já se passaram {ano - 18} anos {mesnasc - 1} meses e {dianasc - 1} dias do alistamento.')











'''
#Se for o dia do alistamento
if ano == 18 and dianasc == 1 and mesnasc == 1:
    print(f'Hoje é seu dia de alistamento!')
    
#Se é um dia antes do alistamento
elif ano == 18 and mesnasc == 1 and dianasc == 2:
    print('Já se passou um dia do alistamento!')

#Se é um mês antes do alistamento
elif ano == 18 and mesnasc == 2 and dianasc == 1:
    print('Já se passou um mês do alistamento!')
#Se é um ano antes do dia do alistamento
elif ano == 17 and mesnasc == 1 and dianasc == 1:
    print('Já se passou um ano do seu alistamento!')
'''



'''
#Se for exatamente um ano depois do alistamento
elif ano == 19 and mesnasc == 1 and dianasc == 1:
    print('Já se passou um ano do seu alistamento!')
    

#Se foi um ano, um mês e um dia depois do alistamento
elif ano == 19 and mesnasc == 2 and dianasc == 2:
    print(f'Já se passaram 1 ano 1 mês e 1 dia do seu alistamento!')
#Se foi um ano e um dia depois do alistamento
elif ano == 19 and dianasc ==2:
    print(f'Já se passaram 1 ano e 1 dia do alistamento')
#Se foi um ano e um mês depois do alistamento
elif ano == 19 and mesnasc ==2:
    print(f'Já se passaram 1 ano e 1 mês do alistamento')

elif ano > 19 and mesnasc > 1 and dianasc > 1:
    print(f'Já se passaram {ano - 18} anos e {mesnasc - 1} meses e {dianasc - 1} dias do seu alistamento!')

elif ano >= 19 and dianasc > 1:
    print(f'Já se passaram {ano - 18} ano e {dianasc - 1} dia do seu alistamento!')

#else:
#   print(f'Faltam {(ano - 18) * -1} anos {mesnasc - 1} meses e {dianasc - 1} dias para o seu alistamento!')
'''