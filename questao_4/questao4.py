
print('Bem vindo a livraria do Nicolas Braga')

# criando variaveis globais
lista_livro = []
id_global = 0

def cadastrar_livro(id):
    global id_global
    
    id_global = id + 1
    
    print('Id Livro: ', id_global)
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    
    # criando lista de dicionario dos livros
    livro = {'id': id_global, 'nome': nome, 'autor': autor, 'editora': editora}
    
    # empurrando o livro para dentro da lista global
    lista_livro.append(livro)
        
def consultar_livro():
  while True:
    print('Escolha a opção desejadada:')        
    print('1 - Consultar todos os Livros')
    print('2 - Consultar Livro por id')
    print('3 - Consultar Livro(s) por autor')
    print('4 - Retornar')
    
    opcao_selecionada = int(input('>>'))
    
    if opcao_selecionada == 1:
        # consultando livros cadastrados
        print('--' * 7)  
        for livro in lista_livro:
           print(f"id: {livro['id']}")
           print(f"nome: {livro['nome']}")
           print(f"autor: {livro['autor']}")
           print(f"editora: {livro['editora']}")
           print('\n')
           
        continue
            
    elif opcao_selecionada == 2:
        # consulta por id
        id_consulta = int(input('Digite o id do livro: '))
        livro_not_found = True
        
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print('\n')
                livro_not_found = False
                break
            
        if livro_not_found == True:
            print('Livro não encontrado')
            
            
            
        continue
        
    elif opcao_selecionada == 3:
        # buscando por autor
        autor = input('Digite o autor do(s) livro(s): ')
        autor_not_found = True
        
        for livro in lista_livro:
            if(livro['autor'] == autor):
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print('\n')
                autor_not_found = False
                
        if autor_not_found == True:
            print('Autor não encontrado')

        continue
                
    else:
        break
    


def remover_livro():
    while True:
        # removendo livro por id
        id_livro = int(input('Digite o id do livro a ser removido: '))
        id_not_found = True  
    
        for livro in lista_livro:
            if livro['id'] == id_livro:
                lista_livro.remove(livro)
                print('Livro removido com sucesso !')
                id_not_found = False
                return
                
            elif id_not_found == True:
                print('Id inválido')
                continue
            
# ciclo do programa
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
        print('--' * 24)
        print('-' * 13, 'MENU REMOVER LIVRO', '-' * 13)
        remover_livro()
    else:
        print('Encerrando programa . . .')
        break