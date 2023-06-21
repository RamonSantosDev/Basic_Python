frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('\033[1mÉ um Palíndromo!\033[m')
else:
    print('\033[1;31mNão é um Palíndromo\033[m')

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('\033[1mÉ um Palíndromo!\033[m')
else:
    print('\033[1;31mNão é um Palíndromo\033[m')''' # Sem uso do 'FOR'