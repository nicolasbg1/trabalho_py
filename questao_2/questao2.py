print("Bem-vindo a Loja de Gelados do Nicolas Braga")
print('--' * 10, 'Cardápio', '--' * 10)
print('--' * 25)
print('---|', '  Tamanho  ', '|  Cupuaçu (CP)  | Açaí (AC)'  , '---|')
print('---|', '     P      |', '    R$  9.00   |', ' R$ 11.00', '---|')
print('---|', '     M      |', '    R$ 14.00   |', ' R$ 16.00', '---|')
print('---|', '     G      |', '    R$ 18.00   |', ' R$ 20.00', '---|')
print('--' * 25)


# acumulador
total = 0


while True:
    sabor_desejado = input('Entre com o sabor desejado (CP/AC): ').upper()
    
    # tratamento caso o sabor_desejado não seja uma das opções requeridas(CP/AC)
    if sabor_desejado not in ['CP', 'AC']:
        print('Sabor inválido. Tente novamente') 
        continue

    tamanho_desejado = input("Entre com o tamanho desejado (P/M/G): ").upper()

    # tratamento caso o tamnho_desejado não seja uma das opções requeridas(P/M/G)
    if tamanho_desejado not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente')
        continue
    
    # verifica o sabor escolhido e segue o fluxo do programa com base nesse dado
    
    if(sabor_desejado == "CP"):
        if(tamanho_desejado == "P"):
            # usei a lógica de escopos para mostrar o preço da opção selecionada pelo usuário ao invés de manipular o total
            valor = 9
            total += 9
        elif(tamanho_desejado == "M"):
            valor = 14
            total+=14
        else:
            valor = 18
            total += 18
        print(f'Você pediu um Cupuaçu no tamanho {tamanho_desejado}: R$ {valor:.2f}')
           
    elif(sabor_desejado == 'AC'):
         if(tamanho_desejado == "P"):
            valor = 11
            total += 11
         elif(tamanho_desejado == "M"):
            valor = 16
            total+=16
         else:
            valor = 20
            total += 20
         print(f'Você pediu um Açaí no tamanho {tamanho_desejado}: R$ {valor:.2f}')
         
         
    #Caso o usuário queira um novo pedido o ciclo do programa irá repedir , caso contrário ele encerra 
    
    novo_pedido = input('Deseja mais alguma coisa? (S/N): ').upper()
    
    if(novo_pedido == 'S'):
        continue
    else:
        print(f'O valor total a ser pago: R${total:.2f}')
        break






        