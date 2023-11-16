def validarCriptografacaoOuDescriptografacao(criptografarOuDescriptografar):
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
    for caractere in mensagem:
        if caractere == ' ':
            caractere = ''

        elif int(caractere) < 0 or int(caractere) > 1:
            print('Digite um código binário válido.')
            mensagem = int(input('Mensagem (com 8 caracteres cada valor e sem espaços.): '))