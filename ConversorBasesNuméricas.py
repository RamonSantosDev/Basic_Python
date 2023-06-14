inteiro = int(input('Digite um valor inteiro: '))
print('''Escolha uma das bases para conversão:
\033[1;36m[ 1 ]\033[m Converter para \033[1;7mBINÁRIO\033[m
\033[1;36m[ 2 ]\033[m Converter para \033[1;7mOCTAL\033[m
\033[1;36m[ 3 ]\033[m Converter para \033[1;7mHEXADECIMAL\033[m''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a \033[1;36m{}\033[m'.format(inteiro, bin(inteiro) [2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a \033[1;36m{}\033[m'.format(inteiro, oct(inteiro) [2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[1;36m{}\033[m'.format(inteiro, hex(inteiro) [2:]))
else:
    print('\033[1;31mOPÇÃO INÁLIDA. Tente novamente\033[m')