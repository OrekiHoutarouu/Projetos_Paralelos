def confirmarSeArquivoExiste(nomeDoArquivo):
    try:
        arquivo = open(nomeDoArquivo, 'rt')
        arquivo.close()
        
    except FileNotFoundError:
        return False
    
    else:
        return True


def criarArquivo(nomeDoArquivo):
    arquivo = open(nomeDoArquivo, 'wt+')
    arquivo.close()


def mostrarArquivo(nomeDoArquivo):
    arquivo = open(nomeDoArquivo, 'rt', encoding = 'utf-8')

    print(f'{"Plataforma:":<35} {"Senha:"}') 
    
    for linha in arquivo:
        plataformaESenha = linha.split(';')
        
        print(f'{plataformaESenha[0]:<35} {plataformaESenha[1]}'.replace('\n', ''))


def cadastrarSenha(nomeDoArquivo, nomeDaPlataforma = 'Desconhecido', senha = 'Desconhecida'):
    arquivo = open(nomeDoArquivo, 'at')
    
    arquivo.write(f'{nomeDaPlataforma};{senha}\n')
    
    print(f'Senha de {nomeDaPlataforma} cadastrada!')