def validarCriptografacaoOuDescriptografacao(criptografarOuDescriptografar):
    """Valida se a opção escolhida pelo usuário é válida ou não.

    Args:
        criptografarOuDescriptografar (int): É a opção escolhida pelo usuário (sendo 1 para criptografar mensagens e 2 para descriptografar mensagens).

    Raises:
        ValueError: Caso o usuário digite um número inteiro menor que 1 ou maior que 2 ou caso o usuário digite uma frase, não um número. 

    Returns:
        int: É a opção escolhida já validada.
    """

    while True:
        try:
            if criptografarOuDescriptografar < 1 or criptografarOuDescriptografar > 2:
                raise ValueError
            
            else:
                break
        
        except ValueError:
                print('\033[0;31mDigite uma opção válida.\033[m')
                criptografarOuDescriptografar = int(input('Opção: '))
    
    return criptografarOuDescriptografar


def validarCodigoBinario(mensagem):
    """Valida se o código binário digitado pelo usuário é válido ou não.
        Sendo que um código binário inválido contém caracteres menores que 0 ou maiores que 1 ou contém caracteres não numéricos.

    Args:
        mensagem (string): É o código binário digitado pelo usuário, que será validado.

    Returns:
        string: É o código binário digitado já validado.
    """
    
    for caractere in mensagem:
        if caractere == ' ':
            caractere = '0'

        if not caractere.isnumeric():
            print('\033[0;31mDigite um código binário válido.\033[m')
            return False

        if int(caractere) < 0 or int(caractere) > 1:
            print('\033[0;31mDigite um código binário válido.\033[m')
            return False
    
    return mensagem


def validarHexadecimal(mensagem):
    """Valida se o código hexadecimal digitado pelo usuário é válido ou não.


    Args:
        mensagem (string): É o código hexadecimal digitado pelo usuário, que será validado

    Returns:
        string: É o código hexadecimal digitado já validado
    """

    for caractere in mensagem:
        if caractere == ' ':
            caractere = '0'

        if not caractere.isalnum():
            print('\033[0;31mDigite um código hexadecimal válido.\033[m')
            return False
        
        elif caractere.isnumeric():
            if int(caractere) < 0 or int(caractere) > 9:
                print('\033[0;31mDigite um código hexadecimal válido.\033[m')
                return False
        
        elif caractere.isalpha():
            if (ord(caractere) < 65 or ord(caractere) > 69) and (ord(caractere) < 97 or ord(caractere) > 101):
                print('\033[0;31mDigite um código hexadecimal válido.\033[m')
                return False
    
    return mensagem