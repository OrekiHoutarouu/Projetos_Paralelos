from os import listdir
from random import choice

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
    letrasMinusculas = 'abcdefghijklmnopqrstuvwxyz'
    letrasMaiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '123456789'
    caracteresEspeciais = '@#$%&.,:;></\?!´`^~[]}{'

    conjuntoDeCaracteres = letrasMinusculas + letrasMaiusculas + numeros + caracteresEspeciais
    senhaForte = ''
    
    print('Senha forte: ', end='')
    for caractere in range(11):
        senhaForte += choice(conjuntoDeCaracteres)

    print(senhaForte)