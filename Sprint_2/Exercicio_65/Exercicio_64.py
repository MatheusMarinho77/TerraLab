primeiroNum = int(input('informe um numero:'))
numeroInfo = 0
soma = primeiroNum
contador = 1

while numeroInfo != 999:
    numeroInfo = int(input('informe outro numero (SE DESEJA SAIR BASTA DIGITAR 999):'))
    soma += numeroInfo
    contador +=1
if numeroInfo == 999:
    soma -= 999
    contador -= 1

print('----------FIM DO PROGRAMA----------')     
print(f'FORAM DIGITADOS {contador} NUMEROS ')
print(f'A SOMA ENTRE ELES FOI DE {soma}')