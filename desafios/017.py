import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
# h = (co**2 + ca**2) ** (1/2)
h = math.hypot(co, ca)
print(f'A hipotenusa do triângulo retângulo é: {h:.2f}')