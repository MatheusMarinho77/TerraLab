from math import pow

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = float(peso/(pow(altura,2)))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25 : 
    print('Peso ideal') 
elif imc >=25 and imc < 30:
    print('Acima do peso')
elif imc >= 30 and imc < 40:
    print('Obeso')
else:
    print('Obesidade morbida') 