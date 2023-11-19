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
                print('Digite uma opção válida.')
                criptografarOuDescriptografar = int(input('Opção: '))
    
    return criptografarOuDescriptografar


def validarCodigoBinario(mensagem):
    """Valida se o código binário digitado pelo usuário é válido ou não (sendo que um código binário inválido contém caracteres menores que 0 ou maiores que 1).

    Args:
        mensagem (string): É o código binário digitado pelo usuário, que será validado.

    Returns:
        string: É o código binário digitado já validado.
    """
        
    for caractere in mensagem:
        if caractere == ' ':
            caractere = ''

        elif int(caractere) < 0 or int(caractere) > 1:
            print('Digite um código binário válido.')
            mensagem = int(input('Mensagem (com 8 bits cada caractere.): '))
    
    return mensagem