print('Bem vindo a Copiadora do Nicolas Braga')
# \n são quebras de linha para espaçar o código
print('\n')

def escolha_servico():
   while True:
    print('Entre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    
    # converte as entradas para maiscula
    servico_escolhido = input('>>').upper()
        
    # verifica se o dado inserido é permitido
    if servico_escolhido not in ['DIG', 'ICO', 'IPB', 'FOT']:
        print('Escolha inválida, entre com  o tipo do serviço novamente')
        print('\n')
        continue
    elif servico_escolhido == 'DIG':
        return 1.10
    elif servico_escolhido == 'ICO':
        return 1
    elif servico_escolhido == 'IPB':
        return 0.40
    else:
        return 0.20

    
    
def num_pagina():
  while True:
    try:
        num_pg = int(input('Entre com o número de páginas: '))
        
        if num_pg >= 20000:
            print('Não aceitamos tantas páginas de uma vez.')
            print('Por favor, entre com o número de páginas novamente')
            print('\n')
            continue
        
        if num_pg  < 20:
            return num_pg
        elif num_pg >= 20 and num_pg < 200:
            desconto = 0.15
            valor_final = num_pg * (1 - desconto)
            return valor_final
        elif num_pg >= 200 and num_pg < 2000:
            desconto = 0.20
            valor_final = num_pg * (1 - desconto)
            return valor_final
        else:
            desconto = 0.25
            valor_final = num_pg * (1 - desconto)
            return valor_final
    except ValueError:
        # exceção caso ocorra uma entrada inválida e um alerta sobre o valor máximo aceito
        print("Por favor, entre com um número inteiro menor a 20000")
        continue

    
def servico_extra():
    while True:
        print('\n')
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada')
        
        try:
            resposta_usuario = int(input('>>'))
            
            if resposta_usuario not in [0, 1, 2]:
                print("Por favor, escolha uma opção válida.")
                continue
            elif resposta_usuario == 0:
                return 0
            elif resposta_usuario == 1:
                return 15
            else:
                return 40
        except ValueError:
            # exceção caso o usuário digite letras e simnbolos que não são permitidos
            print("Por favor, entre com um número inteiro (0/1/2)")
            continue

valor_servico = escolha_servico()
numeros_paginas = num_pagina()
extra = servico_extra()

total = (valor_servico * numeros_paginas) + extra

#  na representação das páginas eu converti para inteiro pois havia caso de vim numeros com casa decimal
print(f'Total: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {int(numeros_paginas)} + extra: {extra:.2f}')
