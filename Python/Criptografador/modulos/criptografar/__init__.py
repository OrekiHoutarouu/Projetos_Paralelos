def criptografarZenitPolar(mensagem):
    
    criptografada = []
    
    for letra in mensagem:
        match(letra):
            case 'z':
                criptografada.append('p')
            case 'p':
                criptografada.append('z')
            case 'e':
                criptografada.append('o')
            case 'o':
                criptografada.append('e')
            case 'n':
                criptografada.append('l')
            case 'l':
                criptografada.append('n')
            case 'i':
                criptografada.append('a')
            case 'a':
                criptografada.append('i')
            case 't':
                criptografada.append('r')
            case 'r':
                criptografada.append('t')
            case 'Z':
                criptografada.append('P')
            case 'P':
                criptografada.append('Z')
            case 'E':
                criptografada.append('O')
            case 'O':
                criptografada.append('E')
            case 'N':
                criptografada.append('L')
            case 'L':
                criptografada.append('N')
            case 'I':
                criptografada.append('A')
            case 'A':
                criptografada.append('I')
            case 'T':
                criptografada.append('R')
            case 'R':
                criptografada.append('T')
            case _:
                criptografada.append(letra)
                
    return f"Criptografada: {''.join(criptografada)}"


def criptografarBinario(mensagem):
    criptografada = []

    for caractere in mensagem:
        criptografada.append(f'{ord(caractere):08b}')
    
    return f"Criptografada: {' '.join(criptografada)}"