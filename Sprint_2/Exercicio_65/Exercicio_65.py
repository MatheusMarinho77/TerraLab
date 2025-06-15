continuar = True
somaNumeros = 0
contador = 0
maior = -9999999999
menor = 1000000000

print('BEM VINDO AO PROGRAMA QUE CALCULA A MEDIA')

while continuar != False:
    numero = int(input('Informe um numero inteiro: '))
    somaNumeros += numero
    contador += 1

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    if contador >= 2:
        validação = int(input('Deseja Continuar?\n\n SIM [1]\n NAO [0]\n')) 
        if validação == 1:
            continue
        elif validação == 0:
            continuar = False
        else:
            print ('Opção invalida, vamos seguir no programa')
            validação = 1

media = float(somaNumeros/contador)

print('A MEDIA DOS NUMEROS:{:.2f}'.format(media))
print('O MAIOR NUMERO :{}'.format(maior))
print('MENOR NUMERO:{}'.format(menor))