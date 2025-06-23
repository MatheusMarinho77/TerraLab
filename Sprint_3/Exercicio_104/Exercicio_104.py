def leiaInt(valores):
    if isinstance(valores,(int,float)):
        print('O numero infomado é valido')        
    else:
       print('O QUE FOI INFORMADO NÃO É UM NUMERO')


valor1 = 120
leiaInt(valor1)

valor2 = 4.55
leiaInt(valor2)

valor3 = False
leiaInt(valor3)

valor4 = 'Ola mundo'
leiaInt(valor4)