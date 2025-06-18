
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
condição = 0

while condição != 5:
    print('\n BEM VINDO AO MENU INICIAL \n')
    print('-----------------------------')
    condição = int(input('Escolha uma das opções abaixo. \n\n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NUMEROS\n[5] SAIR DO PROGRAMA\n'))
    
    if condição == 1:
        soma = valor1 + valor2
        print('\n\n')
        print(f'A SOMA DE {valor1} + {valor2} = {soma}')
    elif condição == 2:
        multiplicação = valor1 * valor2
        print('\n\n')
        print(f'A MULTIPLICAÇÃO DE {valor1} x {valor2} = {multiplicação}')
    elif condição == 3:
        if valor1 >= valor2:
            print('\n\n')
            print(f'O valor {valor1} é maior que o valor {valor2} ')
            print(f'MAIOR : {valor1}')

        else:
            print('\n\n')
            print(f'O valor {valor2} é maior que o valor {valor1} ')
            print(f'MAIOR : {valor2}')
    elif condição == 4:
        print('\n\n')
        print('Informe novos numeros:')
        valor1 = int(input('VALOR 1: '))
        valor2 = int(input('VALOR 2: '))
    

