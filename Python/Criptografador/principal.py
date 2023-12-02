from time import sleep
from modulos import criptografar, descriptografar, utilidades

while True:
    print('='*50)
    print('MENU PRINCIPAL'.center(50))
    print('='*50)

    print('1 - ZENIT POLAR')
    print('2 - Binário')
    print('3 - Hexadecimal')
    print('4 - Sair do programa')

    while True:
        try:
            opcao = int(input('Opção: '))

            if opcao < 1 or opcao > 4:
                raise ValueError
            
            else:
                break

        except ValueError:
            print('\033[0;31mDigite uma opção válida.\033[m')

    print('='*50)

    match opcao:
        case 1:
            print('1 - Criptografar')
            print('2 - Descriptografar')

            criptografarOuDescriptografar = int(input('Opção: '))
            utilidades.validarCriptografacaoOuDescriptografacao(criptografarOuDescriptografar)

            print('='*50)
            
            if criptografarOuDescriptografar == 1:
                print(criptografar.criptografarZenitPolar(mensagem = str(input('Mensagem (sem acentuação): ')).strip()))
                sleep(1.5)

            else:
                print(descriptografar.descriptografarZenitPolar(mensagem = str(input('Mensagem (sem acentuação): ')).strip()))
                sleep(1.5)
        
        case 2:
            print('1 - Criptografar')
            print('2 - Descriptografar')

            criptografarOuDescriptografar = int(input('Opção: '))
            utilidades.validarCriptografacaoOuDescriptografacao(criptografarOuDescriptografar)
            
            print('='*50)
            
            if criptografarOuDescriptografar == 1:
                print(criptografar.criptografarBinario(mensagem = str(input('Mensagem: ')).strip()))
                sleep(1.5)
            
            else:
                mensagem = str(input('Mensagem (com 8 bits cada caractere.): '))
                utilidades.validarCodigoBinario(mensagem)

                print(descriptografar.descriptografarBinario(mensagem))
                sleep(1.5)

        case 3:
            print('1 - Criptografar')
            print('2 - Descriptografar')

            criptografarOuDescriptografar = int(input('Opção: '))
            utilidades.validarCriptografacaoOuDescriptografacao(criptografarOuDescriptografar)

            print('='*50)

            if criptografarOuDescriptografar == 1:
                print(criptografar.criptografarHexadecimal(mensagem = str(input('Mensagem: ')).strip()))
                sleep(1.5)

            else:
                mensagem = str(input('Mensagens (com 2 dígitos cada caractere.): '))

                print(descriptografar.descriptografarHexadecimal(mensagem))
                sleep(1.5)

        case 4:
            print('='*50)
            print('FINALIZANDO PROGRAMA'.center(50))
            print('='*50)

            sleep(2)

            break