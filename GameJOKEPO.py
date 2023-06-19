from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''Sua opção:
\033[1m[1]\033[m PEDRA
\033[1m[2]\033[m PAPEL
\033[1m[3]\033[m TESOURA ''')

jogador = int(input('Qual será sua jogada? '))
print('\033[1m{:=^22}\033[m'.format(''))
print('PC jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[1m{:=^22}\033[m'.format(''))
if pc == 0: #PC jogou PEDRA
    if jogador == 0:
        print('\n\033[1;30;43m EMPATE \033[m')
    elif jogador == 1:
        print('\n\033[1;32m Jogador VENCEU \033[m')
    elif jogador == 2:
        print('\n\033[1;36mPC VENCEU \033[m')
elif pc == 1: #PC jogou PAPEL
    if jogador == 0:
        print('\n\033[1;36mPC VENCEU \033[m')
    elif jogador == 1:
        print('\n\033[1;30;43m EMPATE \033[m')
    elif jogador == 2:
        print('\n\033[1;32m Jogador VENCEU \033[m')
elif pc == 2: #PC jogou tesoura
    if jogador == 0:
        print('\n\033[1;32m Jogador VENCEU \033[m')
    elif jogador == 1:
        print('\n\033[1;36mPC VENCEU \033[m')
    elif jogador == 2:
        print('\n\033[1;30;43m EMPATE \033[m')
