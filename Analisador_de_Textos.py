nome = str(input('Digite seu nome: ')).strip() #Tirar os espaços do nome
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Ao todo seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu 1° Nome tem {} letras.'.format(nome.find(' ')))
