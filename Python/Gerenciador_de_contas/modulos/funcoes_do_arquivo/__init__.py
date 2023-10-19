import os
import json
from modulos import utilidades

def criarPastaComContas(caminho):
    """Cria uma pasta que vai armazenar arquivos .json com as contas cadastradas

    Args:
        caminho (str): É o caminho em que a pasta será criada
    """
    
    try:
        os.mkdir(caminho)
    
    except FileExistsError:
        pass
    
    
def cadastrarContas(caminho, conta):
    """Cadastra uma conta com os dados passados no dicionário "conta" num arquivo .json

    Args:
        caminho (str): É o caminho em que o arquivo .json com os dados da conta será armazenado
        conta (dict): São os dados da conta que vai ser cadastrada no arquivo .json
    """
    
    with open(f'{caminho}/{conta["plataforma"]}.json', 'w+', encoding = 'utf-8') as file:
        json.dump(conta, file, indent = 4)
        
    print(f'Conta de {conta["plataforma"]} cadastrada com êxito.')


def verContasCadastradas(caminho):
    """Mostra as contas cadastradas nos arquivos .json

    Args:
        caminho (str): É o caminho em que as contas a serem mostradas se encontram
    """
    
    print(f'{"  Plataformas:":<35} {"E-mails:":<40} {"Senhas:"}')
    print('-'*100)
    
    numeroDeArquivos = utilidades.contarArquivos(caminho)
    
    if numeroDeArquivos == -1:
        print('Para ver as contas cadastradas é necessário cadastrar uma conta (Opção 1).')

    for indice, conta in enumerate(os.listdir(caminho)):  
        with open(f'{caminho}/{conta}', 'r', encoding = 'utf-8') as file:
            informacao = json.load(file) 
                  
            print(f'{indice + 1} ', end='')
            print(f'{informacao["plataforma"]:<34}', end='')
            print(f'{informacao["email"]:<41}', end='')
            print(f'{informacao["senha"]}')
            
            
def excluirConta(caminho):
    """Exclui alguma conta da pasta "contas"

    Args:
        caminho (str): É o caminho em que a conta que será excluida se encontra
    """
    
    print(f'{"  Plataformas:":<35} {"E-mails:":<40} {"Senhas:"}')
    print('-'*100)
    
    numeroDeArquivos = utilidades.contarArquivos(caminho)
    
    if numeroDeArquivos == -1:
        print('Para excluir alguma conta é necessário cadastrar uma conta (Opção 1).')

    for indice, conta in enumerate(os.listdir(caminho)):  
        with open(f'{caminho}/{conta}', 'r', encoding = 'utf-8') as file:
            informacao = json.load(file) 
                  
            print(f'{indice + 1} ', end='')
            print(f'{informacao["plataforma"]:<34}', end='')
            print(f'{informacao["email"]:<41}', end='')
            print(f'{informacao["senha"]}')
            
    print('-'*100)

    
    while True:
        try:
            qualContaExcluir = int(input('Índice da conta que deseja excluir: ')) - 1 

            if qualContaExcluir > numeroDeArquivos or qualContaExcluir < 0:
                raise ValueError
            
        except ValueError:
            print('Digite uma opção válida.')
        
        else:
            for indice, conta in enumerate(os.listdir(caminho)):
                if indice == qualContaExcluir:
                    os.remove(f'{caminho}/{conta}')
                    print(f'Conta de {conta["plataforma"]} excluída com êxito.')
                    
                    break
            break