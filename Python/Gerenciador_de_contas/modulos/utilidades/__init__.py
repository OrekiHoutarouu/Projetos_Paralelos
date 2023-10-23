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
    """Analisa se a senha do usuário é forte ou não

    Args:
        senha (str): Senha que vai ser analisada pela função
    """

    caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '@#$%&.,:;-+><_/|\()[]}{?!~^`´¨""''']
                                                                                            

    requisitosParaSerUmaSenhaForte = 0
    contemLetraMinuscula = False
    contemLetraMaiuscula = False
    contemNumero = False
    contemCaractereEspecial = False

    for caractereDaSenha in senha:

        if contemLetraMinuscula == False:
            for caractere in caracteres[0]:
                if caractereDaSenha in caractere:
                    requisitosParaSerUmaSenhaForte += 1
                    contemLetraMinuscula = True

        if contemLetraMaiuscula == False:
            for caractere in caracteres[1]:
                if caractereDaSenha in caractere:
                    requisitosParaSerUmaSenhaForte += 1
                    contemLetraMaiuscula = True

        if contemNumero == False:
            for caractere in caracteres[2]:
                if caractereDaSenha in caractere:
                    requisitosParaSerUmaSenhaForte += 1
                    contemNumero = True
                    
        if contemCaractereEspecial == False:
            for caractere in caracteres[3]:
                if caractereDaSenha in caractere:
                    requisitosParaSerUmaSenhaForte += 1
                    contemCaractereEspecial = True

    if len(senha) >= 8:
        requisitosParaSerUmaSenhaForte += 1
        print('Sua senha contém 8 ou mais caracteres.')
    
    else:
        print('Sua senha contém menos de 8 caracteres.')

    if contemLetraMinuscula == True:
        print('Sua senha contém letra(s) minuscula(s).')
    
    else:
        print('Sua senha não contém letra(s) minuscula(s).')
        
    if contemLetraMaiuscula == True:
        print('Sua senha contém letra(s) maiúscula(s).')

    else:
        print('Sua senha não contém letra(s) maiúscula(s)')
        
    if contemNumero == True:
        print('Sua senha contém número(s)')
    
    else:
        print('Sua senha não contém número(s)')
        
    if contemCaractereEspecial == True:
        print('Sua senha contém caractere(s) especial(is).')
    
    else:
        print('Sua senha não contém caractere(s) especial(is).')

    print(f'Sendo assim, sua senha atinge {requisitosParaSerUmaSenhaForte} dos 5 requisitos para ser uma senha forte, portanto:')

    match requisitosParaSerUmaSenhaForte:
        case 1:
            print('Sua senha é fraca.')
        
        case 2:
            print('Sua senha está entre média e fraca.')

        case 3:
            print('Sua senha é média.')
        
        case 4:
            print('Sua senha está entre média e forte.')

        case 5:
            print('Sua senha é forte')

        case _:
            print('Senha com caracteres desconhecidos ou não digitados.')


def gerarSenhaForte():
    """Gera senha forte totalmente aleatória para o usuário
    """

    caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '@#$%&.,:;-+><_/|\()[]}{?!~^`´¨""''']

    print('Senha forte: ', end='')

    for caractere in caracteres:
        caractere = list(caractere.strip())

        shuffle(caractere)

        resultado = ''.join(caractere)
        print(resultado[:3], end='')
        
    print('\nContém 12 caracteres, duplamente sorteados, sendo eles:\n 3 letras minúsculas\n 3 letras maiúsculas\n 3 números inteiros\n 3 caracteres especiais.')