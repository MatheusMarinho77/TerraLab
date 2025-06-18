continuar = True
contador18 = 0
contadorHomens = 0
contadorMulheres20 = 0

while continuar != False:
    print('------------CADASTRO PESSOA------------')
    idade = int(input('Informe a idade: '))
    sexo = str(input('INFORME O SEXO:\nMASCULINO [M]\nFEMININO [F]')).upper()
    if sexo == 'M':
        contadorHomens += 1
    if sexo == 'F' and idade < 20:
        contadorMulheres20 += 1   
    if idade >= 18:
        contador18 += 1
    print()
    parar = input('DESEJA CONTINUAR? [S/N]').upper()
    if parar == 'N':
        break

print('----------------------------------------------------') 
print(F'MAIORES DE IDADE : {contador18}')  
print(f'HOMENS CADASTRADOS: {contadorHomens}')
print(f'MULHER ABAIXO DE 20 ANOS: {contadorMulheres20}')

