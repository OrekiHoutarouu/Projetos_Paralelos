def confirmaSeArquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True