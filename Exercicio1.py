## - Escreva um algoritmo que solicite um número ao usuário. 
##Caso seja digitado um valor entre 0 e 9, mostre: “valor correto”, caso contrário 
##mostre: “valor incorretoc. 

numero = float(input('Digite um numero? '))
if numero < 9:
    print('Valor correto')
else:
    print('Valor incorreto')

perguntaNumero = input('Qual é o seu numero favorito?')
if numero ==10:
    print('Você acertou')
else:
    print('Você errou')
    