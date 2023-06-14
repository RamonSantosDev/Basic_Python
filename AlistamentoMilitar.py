from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc
print('Quem nasceu em \033[1m{}\033[m tem \033[1m{}\033[m anos em \033[1m{}\033[m.\n'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam \033[1;33m{}\033[m anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamneto será em \033[1;33m{}\033[m'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Deveria ter se alistando há \033[1;33m{}\033[m ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamneto foi em \033[1;33m{}\033[m'.format(ano))