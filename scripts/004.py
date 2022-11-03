try:
    a = open('myfile.txt', 'rt')
    a.close()
except FileNotFoundError:
    print('nâo')
else:
    print('sim')