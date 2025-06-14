print('Verificador de frases palindromas')

frase = str(input('Digite uma frase:').upper())
frase = frase.replace(" ", "")
palindromo = frase[::-1]

if frase == palindromo:
    print('A palavra é um palindromo!!!')
else :
    print('A frase/palavra nao é um palindromo.\nFrase Original:{}\nInverso dela:{}'.format(frase,palindromo))
