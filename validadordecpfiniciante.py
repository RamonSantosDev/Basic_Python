print('Informe o CPF ')
cpf = input()

cpf = cpf.replace('.','').replace('-','')

# conversão sem tratamento de erro intencional
if len(cpf) != 11:
    print('CPF INVÁLIDO')
    exit()

num1 = int(cpf[0])
num2 = int(cpf[1])
num3 = int(cpf[2])
num4 = int(cpf[3])
num5 = int(cpf[4])
num6 = int(cpf[5])
num7 = int(cpf[6])
num8 = int(cpf[7])
num9 = int(cpf[8])
num10 = int(cpf[9])
num11 = int(cpf[10])

#Se os números forem iguais o CPF será inválido
if num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == num10 == num11:
    print('CPF INVÁLIDO')
    exit()

primeira_soma = num1*10 + num2*9 + num3*8 + num4*7 + num5*6 + num6*5 + num7*4 + num8*3 + num9*2

primeira_digt_verif = (primeira_soma*10) % 11

#Se o resto do primeira_digt_verif for '10' corvente para '0'
if primeira_digt_verif == 10:
    primeira_digt_verif = 0

segunda_soma = num1*11 + num2*10 + num3*9 + num4*8 + num5*7 + num6*6 + num7*5 + num8*4 + num9*3 + primeira_digt_verif*2
segundo_digt_verif = (segunda_soma*10) % 11

if (primeira_digt_verif == num10 and  segundo_digt_verif == num11):
    print('CPF Válido')
else:
    print('Digitos Verificadores inválidos')

print('Validação concluída')