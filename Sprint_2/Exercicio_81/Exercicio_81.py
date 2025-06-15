lista = []
numerosNaLista = int(input('Informe quantos numeros deseja colocar na lista.'))

for i in range(numerosNaLista):
    valor = int(input('Digite um valor:'))
    lista.append(valor) 

print(f'O tamanho da lista é de {len(lista)}')
print('O numero 5 esta presenta na lista?')
print(f'{5 in lista}')     