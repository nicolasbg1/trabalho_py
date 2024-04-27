
print('Bem vindo a Loja do Nicolas Braga')

# valores recebidos
produto = float(input("Entre com o valor do produto: "))
quant = int(input("Entre com a quantidade do produto: "))

# Calculo para o valor do produto sem desconto
valor_produto = produto * quant 

#Condição para aplicar desconto 
if valor_produto < 2500:
    desconto = 0
elif valor_produto >= 2500 and valor_produto < 6000:
    desconto =  0.04
elif valor_produto >= 6000 and valor_produto < 10000 :
    desconto = 0.07
else:
    desconto = 0.11

# valor com desconto aplicado
valor_produto_com_desconto = valor_produto * (1 - desconto)


print(f'O valor SEM desconto: R${valor_produto:.2f}')
print(f'O valor COM desconto: R${valor_produto_com_desconto:.2f}')        
