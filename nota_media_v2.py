nota1=float(input('Informe a primeira nota: '))
nota2=float(input('Informe a segunda nota: '))

#calcule a media
media=(nota1 + nota2)/2

#verificação
if media >= 7.0:
    print('A media: %.1f - aprovado'% media)
else:
    print('A media: %.1f - Reprovado' % media)