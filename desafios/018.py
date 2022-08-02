import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print(f'O ângulo {an} tem o SENO de {seno:.2f}.')
cosseno = math.cos(math.radians(an))
print(f'O ângul de {an} tem COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an} tem TANGENTE de {tangente:.2f}')