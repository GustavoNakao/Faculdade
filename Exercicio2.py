#Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a 
#quantidade de horas trabalhadas, calcule e mostre o valor do salário. 
#Considere os valores de horas a seguir, de acordo com o turno de trabalho. 
#Caso o turno seja igual a ‘N’ (utilize um caractere para representar) 
#o valor da hora trabalhada é R$ 45,00, caso contrário é R$ 37,50

turnoTrabalho = float(input('Qual seu turno de trabalho? '))
quantidadeTrabalho = float(input('Qual e a quantidade de horas trabalhadas? '))
    
if turnoTrabalho == 45.00:
    print('O valor e igual a 45,00')
else:
    print('O valor e de 37,50')
    