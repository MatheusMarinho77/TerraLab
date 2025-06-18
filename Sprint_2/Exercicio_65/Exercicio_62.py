
n = int(input('INFORME UM NUMERO QUALQUER: '))
pa = int(input('QUAL SERA SUA PA?'))
p = pa
contador = 1

print(n)

while contador < 11:
    if contador == 1:
        p = n + pa
        print(p)
        contador += 1
    else:
        p = p + pa
        print(p)
        contador += 1
    
maisTermos = int(input('VOCE DESEJA VER MAIS QUANTOS TERMOS? '))

while maisTermos != 0:
    p = p + pa
    print(p)
    maisTermos -= 1
