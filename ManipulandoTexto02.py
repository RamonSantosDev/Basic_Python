# Separar digitos de um número
num = int(input('Digite um número de 0 á 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Verificando a primeiras palavra de um texto
cid = str(input('Cidade que nasceu: ')).strip()
print(cid[0:5].upper() == 'SANTO')

# Programa para saber se o nome tem silva
nome = str(input("Seu nome: ")).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
