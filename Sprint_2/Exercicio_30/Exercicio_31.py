## Calculadora de preço da viagem

distanciaPercorrida = int(input('Informe a distancia em KM da viagem: '))

if distanciaPercorrida <= 200:
    valorViagem = float(distanciaPercorrida * 0.50)
    print('Custo da viagem é de: R${:.2f}'.format(valorViagem))
else:
    valorViagem = float(distanciaPercorrida * 0.45)
    print('Custo da viagem é de: R${:.2f}'.format(valorViagem))
print('O viagem tem a distancia de {} e seu valor de R${:.2f} preço '.format(distanciaPercorrida, valorViagem))
