velocidade = float(input('Velocidade do seu carro: '))
if velocidade > 80:
        multa = (velocidade-80) * 7
        print('Você foi MULTADO R${}'.format(multa))
print('Boa viagem')