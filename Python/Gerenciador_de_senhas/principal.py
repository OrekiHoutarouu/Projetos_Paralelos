from Funcoes_do_arquivo import *
from time import sleep

arquivo = 'Senhas.txt'

if confirmarSeArquivoExiste(arquivo) == False:
    criarArquivo(arquivo)
    
print('='*50)
print('MENU PRINCIPAL'.center(50))
print('='*50)

print('1 - Ver senhas cadastradas')
print('2 - Cadastrar nova senha')
print('3 - Sair do programa')

while True:
    while True:
        try:
            opcao = int(input('Opção: '))
            
            if opcao < 1 or opcao > 3:
                print('Por favor, digite uma opção válida')
                
        except:
            print('Por favor, digite uma opção válida')
        
        else:
            break
    
    if opcao == 1:
        print('='*50)
        print('SENHAS CADASTRADAS'.center(50))
        print('='*50)
        
        mostrarArquivo(arquivo)
        print('='*50)
    
    elif opcao == 2:
        print('='*50)
        print('CADASTRAR SENHA'.center(50))
        print('='*50)
        
        nomeDaPlataforma = str(input('Plataforma: '))
        senha = str(input('Senha: '))
        
        cadastrarSenha(arquivo, nomeDaPlataforma, senha)
        print('='*50)
        
    elif opcao == 3:
        print('='*50)
        print('SAINDO DO PROGRAMA'.center(50))
        print('VOLTE SEMPRE!'.center(50))
        print('='*50)
        
        sleep(2)
        
        break 