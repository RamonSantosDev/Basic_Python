somaidade = 0
mediaidade = 0
velhohomem = 0
nomevelho = ''
mulher20 = 0
for p in range(1, 5):
    print('----- {}°Pessoa -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade               # Somar todas as idades

    if p == 1 and sexo in 'M':       # O nome do homem mais velho
        velhohomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > velhohomem:
        velhohomem = idade
        nomevelho = nome

    if sexo in 'F' and idade < 20:    # Quantas mulheres têm menos de 20 anos
        mulher20 += 1

mediaidade = somaidade/4              # Media da idades das 4 Pessoas

print('A média de idade do grupo é \033[1m{}\033[m'.format(mediaidade))
print('Homem velho tem \033[1m{}\033[m anos e se chama \033[1m{}\033[m'.format(velhohomem, nomevelho))
print('São \033[1m{}\033[m mulheres com menos de 20 anos.'.format(mulher20))'''
