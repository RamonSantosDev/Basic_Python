'''
Um programa que receba as medidas dos lados de um triangulo e
diga se ele é equilatero, isosceles ou escaleno;
'''
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if(lado1 == lado2 and lado2 == lado3):
    print('Equilátero')
elif(lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print('Isosceles')
else:
    print('Escaleno')