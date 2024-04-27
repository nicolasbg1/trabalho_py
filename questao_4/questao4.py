
print('Bem vindo a livraria do Nicolas Braga')

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    global id_global
    
    nome = input("Por favor entre com o nome do livro: ")
    
    autor = input("Por favor entre com o autor do livro: ")
    
    editora = input("Por favor entre com a editora do livro: ")
    
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    
    lista_livro.append(livro)
    
    id_global += 1
    
def consultar_livro():
    print('Escolha a opção desejadada:')        
    print('1 - Consultar todos os Livros')
    print('2 - Consultar Livro por id')
    print('3 - Consultar Livro(s) por autor')
    print('4 - Retornar')
    
    opcao_selecionada = int(input('>>'))
    
    if opcao_selecionada == 1:
        for livro in lista_livro:
            print(livro)
    elif opcao_selecionada == 2:
        id_consulta = int(input(''))    
    




def remover_livro():
    print('1')    
    
while True:
    print('--' * 24)
    print('--' * 8 , 'MENU PRINCIPAL', '--' * 8)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')
    
    opcao_selecionada = int(input('>>'))
    
    if opcao_selecionada not in [1, 2, 3, 4]:
        print('Opção inválida')
        continue
    
    if opcao_selecionada == 1:
        print('--' * 24)
        print('-' * 13 , 'MENU CADASTRAR LIVRO', ('-' * 13) )
        cadastrar_livro(id_global)
    elif opcao_selecionada == 2:
        print('--' * 24)
        print('-' * 13, 'MENU CONSULTAR LIVRO', '-' * 13)
        consultar_livro()
    elif opcao_selecionada == 3:
        remover_livro()
    else:
        print('Encerrando programa . . .')
        break