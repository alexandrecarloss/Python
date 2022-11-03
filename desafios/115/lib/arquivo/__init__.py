def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True