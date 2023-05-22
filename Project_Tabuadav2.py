from time import sleep
print(40*'=')
print('Boas vindas ao meu 1° Projeto!👨🏻‍💻')
print(40*'=')

nome = input('\nDigite seu nome: ')
print('Iniciando calculadora...')
sleep(3)

print(f'Calculadora iniciada! E ai {nome} bora começar?  ')

continua = 's'
while(continua == 's'):
    num1 = float(input('\nDigite um 1°Número:  '))
    op = input('Digite a Operação ( + | - | * | / ): ')
    num2 = float(input('Digite o 2°Número: '))

    if(op == '+'):
        resultado = num1 + num2
        print(f'\nA soma de {num1} + {num2} = {resultado}\n')
    elif(op == '-'):
        resultado = num1 - num2
        print(f'\nA subtração de {num1} - {num2} = {resultado}\n')
    elif(op == '*'):
        resultado = num1 * num2
        print(f'\nA multiplicação de {num1} * {num2} = {resultado}\n')
    elif(op == '/'):
        resultado = num1 / num2
        print(f'\n A Divisão de {num1} / {num2} = {resultado:.2f}\n')
    else:
        print('❌ERRO❌')

    continua = input('Deseja continuar?(s/n): ')
