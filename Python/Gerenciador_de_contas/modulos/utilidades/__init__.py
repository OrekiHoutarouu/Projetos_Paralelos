from os import listdir

def contarArquivos(caminho):
    """Conta quantos arquivos .json estão presentes na pasta "contas"

    Args:
        caminho (str): É o caminho em que vão ser contados os arquivos .json
    """
    
    numeroDeArquivos = -1
    
    for indice in enumerate(listdir(caminho)):
        numeroDeArquivos += 1
    
    return numeroDeArquivos