#3- Faça um programa em Python que obtenha o valor de uma compra, 
#calcular e mostrar o valor da compra considerando o desconto, 
#conforme descrito abaixo: 
#para compras acima de R$ 200 a loja dá um desconto de 20%
#para as abaixo disso não tem desconto, mostre o valor da compra. 

valorCompra = float(input('Qual e o valor da sua compra? '))
descontoCompra = valorCompra * 0.2

if valorCompra >= 200:
    print(f'Vc ganhou um desconto de {descontoCompra} reais')
else:
    print(f'O senhor não possui desconto, sua compra foi de {valorCompra} reais')



