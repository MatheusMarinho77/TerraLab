p1 = 0
p2 = 1
sequencia = 2   

numeroTermos = int(input('Informe o numero de termos da sequencia de Fibonacci: '))
print(f'{p1}\n{p2}')

while sequencia < numeroTermos:
    prox = p1 + p2
    p1 = p2
    p2 = prox
    print(prox)
    sequencia +=1
