from os import listdir
from random import shuffle
import re

def contarArquivos(caminho):
    """Conta quantos arquivos .json estão presentes na pasta "contas"

    Args:
        caminho (str): É o caminho em que vão ser contados os arquivos .json
    """
    
    numeroDeArquivos = -1
    
    for indice in enumerate(listdir(caminho)):
        numeroDeArquivos += 1
    
    return numeroDeArquivos


def analisarSenhaForte(senha):
    caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '123456789', '@#$%&.,:;></\?!']

    requisitosParaSerUmaSenhaForte = 0

    for caractereDaSenha in senha:
        for caractere in caracteres[0]:
            if caractereDaSenha in caractere:
                requisitosParaSerUmaSenhaForte += 1
                break
        break

    for caractereDaSenha in senha:
        for caractere in caracteres[1]:
            if caractereDaSenha in caractere:
                requisitosParaSerUmaSenhaForte += 1
                break
        break

    for caractereDaSenha in senha:
        for caractere in caracteres[2]:
            if caractereDaSenha in caractere:
                requisitosParaSerUmaSenhaForte += 1
                break
        break
    
    for caractereDaSenha in senha:
        for caractere in caracteres[3]:
            if caractereDaSenha in caractere:
                requisitosParaSerUmaSenhaForte += 1
                break
        break

    match requisitosParaSerUmaSenhaForte:
        case 1:
            print('Sua senha é fraca')
        
        case 2:
            print('Sua senha está entre média e fraca')

        case 3:
            print('Sua senha é média')
        
        case 4:
            print('Sua senha é forte')


def sugerirSenhaForte():
    caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '123456789', '@#$%&.,:;></\()[]}{?!~^`´']

    print('Senha forte: ', end='')

    for caractere in caracteres:
        caractere = list(caractere.strip())

        shuffle(caractere)

        resultado = ''.join(caractere)
        print(resultado[:3], end='')

    print('\nContém 12 caracteres, sendo eles:\n 3 letras minúsculas\n 3 letras maiúsculas\n 3 números inteiros\n 3 caracteres especiais.')