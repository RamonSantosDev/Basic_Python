n = int(input('Um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='\033[m')

print('\nO número {} foi divisível \033[1;33m{}\033[m vezez.'.format(n, tot), end=' ')
if tot == 2:
    print('\033[1mO número é PRIMO\033[m')
else:
    print('Não é PRIMO')