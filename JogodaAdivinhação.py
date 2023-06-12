from random import randint
n = randint(0, 5) # Computador pensar algum N°
r = int(input('Adivinhe um numero de 0 á 5: ')) # Jogador tenta adivinhar
if r == n:
        print('Você acertou! o número foi {}'.format(n))
else:
        print('Errou o número, não era {} e sim {}'.format(r, n))