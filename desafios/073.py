times = ('Palmeiras', 	
'Flamengo', 	
'Corinthians', 	
'Fluminense', 	
'Athletico-PR', 'Internacional', 	
'Atlético-MG', 	
'América-MG', 	
'Bragantino', 	
'Santos', 	
'São Paulo', 	
'Botafogo', 	
'Goiás', 'Ceará', 	
'Fortaleza', 	
'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 	
'Juventude')
print('-=' * 50)
print(f'Times do Brasileirão: {times}')
print('-=' * 50)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=' * 50)
print(f'Os 4 últimos são: {times[16:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
#Chapecoence
if 'Chapecoence' in times:
    print(f'O Chapecoence está na {times.index("Chapecoence") + 1}° posição.')
else:
    print(f'O Chapecoence não está na série a')

