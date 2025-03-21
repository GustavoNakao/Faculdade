#Escreva um programa em Python que solicite ao usuário os valores de três contas de consumo 
#(p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é suficiente para pagar as três contas, caso não seja apresente a mensagem 
#“Salário insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.

contaAgua = float(input('Qual e o valor da sua conta de agua? '))
contaLuz = float(input('Qual e o valor da conta de Luz? '))
contaTelefone = float(input('Qual e o valor da conta de telefone? '))
apresentarSalario = float(input('Qual e o seu salario? '))

contasPagar = contaTelefone + contaLuz + contaAgua

if apresentarSalario >= contasPagar:
    print(f'O valor gasto foi de ${apresentarSalario - contasPagar}')
else:
    print('#“Salário insuficiente!”')
