from modulos import funcoes_do_arquivo, utilidades
import os
from time import sleep

caminho = os.path.join('./', 'contas')
funcoes_do_arquivo.criarPastaComContas(caminho)

while True:  
    print('='*100)
    print('MENU PRINCIPAL'.center(100))
    print('='*100)

    print('1 - Cadastrar nova conta')
    print('2 - Ver contas cadastradas')
    print('3 - Deletar alguma conta')
    print('4 - Analisar se sua senha é forte')
    print('5 - Gerar senha forte')
    print('6 - Sair do programa')
    
    while True:
        try:
            opcao = int(input('Opção: '))
            
            if opcao > 6 or opcao < 1:
                raise ValueError
                
            else:
                break
            
        except ValueError:
            print('Digite uma opção válida.')
                
    match opcao:
        case 1:
            print('='*100)
            print('CADASTRAR NOVA CONTA'.center(100))
            print('='*100)
            
            funcoes_do_arquivo.cadastrarContas(caminho, conta = {
                    'plataforma': str(input('Plataforma: ')),
                    'email': str(input('E-mail: ')),
                    'senha': str(input('Senha: '))
                    }
            )
            
            sleep(1.5)
        
        case 2:
            print('='*100)
            print('VER CONTAS CADASTRADAS'.center(100))
            print('='*100)
            
            funcoes_do_arquivo.verContasCadastradas(caminho)
            sleep(2)
                
        case 3:
            print('='*100)
            print('EXCLUIR CONTA'.center(100))
            print('='*100)
            
            funcoes_do_arquivo.excluirConta(caminho)
            sleep(2)

        case 4:
            print('='*100)
            print('ANALISAR SE SENHA É FORTE'.center(100))
            print('='*100)

            utilidades.analisarSenhaForte(str(input('Senha: ')))
            sleep(2)
            
        case 5:
            print('='*100)
            print('GERAR SENHA FORTE'.center(100))
            print('='*100)
            
            print(utilidades.gerarSenhaForte())
            print('\nContém 12 caracteres, duplamente e aleatoriamente sorteados, sendo eles:\033[0;32m\n 3 letras minúsculas\n 3 letras maiúsculas\n 3 números inteiros\n 3 caracteres especiais.\033[m')
            sleep(2)

        case 6:
            print('='*100)
            print('FINALIZANDO PROGRAMA'.center(100))
            print('='*100)
            
            sleep(2)
            
            break