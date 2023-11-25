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
        
    print(f'\033[0;32mConta de {conta["plataforma"]} cadastrada com êxito.\033[m')


def verContasCadastradas(caminho):
    """Mostra as contas cadastradas nos arquivos .json

    Args:
        caminho (str): É o caminho em que as contas a serem mostradas se encontram
    """
    
    print(f'{"  Plataformas:":<35} {"E-mails:":<40} {"Senhas:"}')
    print('-'*100)
    
    numeroDeArquivos = utilidades.contarArquivos(caminho)
    
    if numeroDeArquivos == -1:
        print('\033[0;31mPara excluir visualizar ou excluir alguma conta é necessário primeiro cadastrar uma conta (Opção 1).\033[m')
        
    else:
        for indice, conta in enumerate(os.listdir(caminho)):  
            with open(f'{caminho}/{conta}', 'r', encoding = 'utf-8') as file:
                informacao = json.load(file) 
                    
                print(f'{indice + 1} ', end='')
                print(f'{informacao["plataforma"]:<34}', end='')
                print(f'{informacao["email"]:<41}', end='')
                print(f'{informacao["senha"]}')
                
        print('-'*100)
            
            
def excluirConta(caminho):
    """Exclui alguma conta da pasta "contas"

    Args:
        caminho (str): É o caminho em que a conta que será excluida se encontra
    """
    
    numeroDeArquivos = utilidades.contarArquivos(caminho)
    verContasCadastradas(caminho)
    
    if numeroDeArquivos != -1:
        while True:
            try:
                qualContaExcluir = int(input('Índice da conta que deseja excluir: ')) - 1 

                if qualContaExcluir > numeroDeArquivos or qualContaExcluir < 0:
                    raise ValueError
                
            except ValueError:
                print('\033[0;31mDigite uma opção válida.\033[m')
            
            else:
                for indice, conta in enumerate(os.listdir(caminho)):
                    if indice == qualContaExcluir:
                        os.remove(f'{caminho}/{conta}')
                        
                        print(f'\033[0;32mConta de {conta[:-5]} excluída com êxito.\033[m')
                        
                        break
                break