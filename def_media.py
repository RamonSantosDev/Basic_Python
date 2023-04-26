def lernotas():
    n=float(input('Digite uma nota para o aluno: '))
    return n


def resultado(n1,n2):
    media=(n1+n2)/2
    print('nota1: ',n1)
    print('nota2: ', n2)
    print('Media: ',media, 'Resultado: ', end='')
    if media >=7:
        print('APROVADO')
    else:
        print('REPROVADO')


a=lernotas()
b=lernotas()
resultado(a,b)