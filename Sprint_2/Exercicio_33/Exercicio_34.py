
salario = float(input('Informe seu salario: '))

if salario > 1250:
    novoSalario = float(salario * 1.10)
    print('O novo salario teve um aumento de 10% e seu novo salario sera de R${:.2f} '.format(novoSalario))  
elif salario <= 1250:
    novoSalario = float(salario * 1.15)
    print('O novo salario teve um aumento de 15% e  seu novo salario sera de R${:.2f} '.format(novoSalario))  
