tecla = 's'
while tecla == 's' or tecla == 'S':
    i = 0
    valor = int(input('Digite um valor inteiro: '))
    while i <= 10:
        print(valor,'x',i,'=',valor*i)
        i = i + 1
    tecla = input('\nDeseja continuar a conta (s) / (n) ]: ')
    while tecla != 'N' and tecla != 'n' and tecla != 's' and tecla != 'S':
        tecla = input('\n(n;N) Para sair / (s;S) para voltar: ')

else:
    print('\nTerminou seu programa !')