from os import listdir
from random import shuffle


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

    requisitosSenhaForte = 0
    contemLetraMinuscula = False
    contemLetraMaiuscula = False
    contemNumero = False
    contemCaractereEspecial = False

    for caractereDaSenha in senha:

        if contemLetraMinuscula == False:
            if caractereDaSenha.islower():
                contemLetraMinuscula = True
                requisitosSenhaForte += 1

        if contemLetraMaiuscula == False:
            if caractereDaSenha.isupper():
                contemLetraMaiuscula = True
                requisitosSenhaForte += 1

        if contemNumero == False:
            if caractereDaSenha.isnumeric():
                contemNumero = True
                requisitosSenhaForte += 1
                    
        if contemCaractereEspecial == False:
            if not caractereDaSenha.isalnum():
                contemCaractereEspecial = True
                requisitosSenhaForte += 1

    if len(senha) >= 8:
        requisitosSenhaForte += 1
        print('\033[0;32mSua senha contém 8 ou mais caracteres.\033[m')
    
    else:
        print('\033[0;31mSua senha não contém 8 ou mais caracteres.\033[m')

    if contemLetraMinuscula == True:
        print('\033[0;32mSua senha contém letra(s) minuscula(s).\033[m')
    
    else:
        print('\033[0;31mSua senha não contém letra(s) minuscula(s).\033[m')
        
    if contemLetraMaiuscula == True:
        print('\033[0;32mSua senha contém letra(s) maiúscula(s).\033[m')

    else:
        print('\033[0;31mSua senha não contém letra(s) maiúscula(s)\033[m')
        
    if contemNumero == True:
        print('\033[0;32mSua senha contém número(s)\033[m')
    
    else:
        print('\033[0;31mSua senha não contém número(s)\033[m')

    if contemCaractereEspecial == True:
        print('\033[0;32mSua senha contém caractere(s) especial(is).\033[m')
    
    else:
        print('\033[0;31mSua senha não contém caractere(s) especial(is).\033[m')

    return requisitosSenhaForte


def gerarSenhaForte():
    """Gera senha forte totalmente aleatória para o usuário
    """

    caracteres = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '@#$%&.,:;-+><_/|\()[]}{?!~^`´¨""''']

    print('Senha forte: ', end='')
    resultado = []

    for caractere in caracteres:
        caractere = list(caractere.strip())

        shuffle(caractere)

        resultado.append(''.join(caractere[:3]))

        resultado = list(''.join(resultado))

        shuffle(resultado)

    return ''.join(resultado)