def descriptografarZenitPolar(mensagem):
    """Descriptografa mensagens escritas em ZENIT POLAR (sistema simples de criptografia que substitui as letras no nome ZENIT POLAR) 
        para a mensagem no texto claro. 
        Não reconhece acentuação, porém reconhece símbolos e emojis.

    Args:
        mensagem (string): É o texto cifrado, em ZENIT POLAR, que será descriptografado para a mensagem no texto claro. 

    Returns:
        list: É o texto cifrado já descriptografado para o texto claro.
    """
    
    descriptografada = []
    
    for letra in mensagem:
        match(letra):
            case 'z':
                descriptografada.append('p')
            case 'p':
                descriptografada.append('z')
            case 'e':
                descriptografada.append('o')
            case 'o':
                descriptografada.append('e')
            case 'n':
                descriptografada.append('l')
            case 'l':
                descriptografada.append('n')
            case 'i':
                descriptografada.append('a')
            case 'a':
                descriptografada.append('i')
            case 't':
                descriptografada.append('r')
            case 'r':
                descriptografada.append('t')
            case 'Z':
                descriptografada.append('P')
            case 'P':
                descriptografada.append('Z')
            case 'E':
                descriptografada.append('O')
            case 'O':
                descriptografada.append('E')
            case 'N':
                descriptografada.append('L')
            case 'L':
                descriptografada.append('N')
            case 'I':
                descriptografada.append('A')
            case 'A':
                descriptografada.append('I')
            case 'T':
                descriptografada.append('R')
            case 'R':
                descriptografada.append('T')
            case _:
                descriptografada.append(letra)
                
    return f"Descriptografada: {''.join(descriptografada)}"


def descriptografarBinario(mensagem):
    """Descriptografa mensagens escritas em código binário (sistema de numeração que utiliza a base 2) para seu correspondente no Unicode. 
        Utiliza o Unicode para reconhecer todos os caracteres, incluindo caracteres acentuados, símbolos e emojis.

    Args:
        mensagem (string): É o texto cifrado, em código binário, que será descriptografado para o texto claro. 

    Returns:
        list: É o texto cifrado já descriptografado para o texto claro.
    """

    descriptografada = []
    bytes = []
    byte = []
    contador = 0

    for caractere in mensagem:
        if caractere == ' ':
            caractere = ''
            contador -= 1

        byte.append(caractere)
        contador += 1

        if contador == 8:
            bytes.append(''.join(byte)[:])
            byte.clear()
            contador = 0
    
    for byte in bytes:
        byte = int(byte, 2)
        descriptografada.append(chr(int(byte)))

    return f"Descriptografada: {''.join(descriptografada)}"