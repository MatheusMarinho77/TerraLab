
numero = int(input('Informe um numero para que eu possa fazer seu fatorial: '))
contFatorial = numero - 1
contadorLaço = 0

while contFatorial != 0:
    if contadorLaço == 0:
        fatorial = numero * contFatorial
        contFatorial -= 1
        contadorLaço+=1
    else:
        fatorial = fatorial * contFatorial
        contFatorial -= 1

print(f'O fatorial de {numero} é = {fatorial}')       
    
    