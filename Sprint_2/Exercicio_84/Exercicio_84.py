pessoas = list()
contador = 1
maior_peso = -999
menor_peso = 100

print('Bem-vindo ao programa de cadastro de pessoas e pesos!')
print('Se deseja sair do programa basta Digitar "sair"')

while True:
    nome = str(input('Digite o nome da pessoa: ')).capitalize()
    if nome == 'Sair':
        contador += -1
        break 
    
    peso = float(input(f'Digite o peso de {nome} (em kg): '))
    pessoa = {"nome": nome, "peso": peso}
    pessoas.append(pessoa)
    print(f'{nome} cadastrado(a) com sucesso!\n\n')
    contador +=1

    for p in pessoas:
        if p['peso'] > maior_peso:
            maior_peso = p['peso']
            nome_mais_pesado = p['nome']
        
        if p['peso'] < menor_peso:
            menor_peso = p['peso']
            nome_mais_leve = p['nome']

print(f'Foram cadastradas {contador} pessoas')
print(f'A pessoa mais pesada pesa {maior_peso}')
print(f'A pessoa mais leve pesa {menor_peso}')