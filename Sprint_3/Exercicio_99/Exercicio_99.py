def maior(num):
    maior = -99999999
    for i in num:
        if i >= maior:
            maior = i
    print(f'O maior numero da lista {num} é: {maior}') 
    print('-'*30)       


lista1 = [34,55,1,0,7,33,107,00,10]
lista2 = [10,1977,2024,1,2121]
lista3 = [30,7,9,5,9,66,4,3]
lista4 = [33,45,77,1,3,41,24]

maior(lista1)
maior(lista2)
maior(lista3)
maior(lista4)

    