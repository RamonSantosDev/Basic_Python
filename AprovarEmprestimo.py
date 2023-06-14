casa = float(input('Valor da casa:R$'))
salario = float(input('Seu salario:R$ '))
anos = int(input('Quantos anos de finaciamento?: '))
prestação = casa / (anos * 12)
minimo = salario * 30/100 #não pode exceder 30% do salário

print('\nPara pagar uma casa de R${:.2f} em {} anos'.format(casa, anos),end='')
print(' a prestação será de \033[1;7mR${:.2f}\033[m ao mês'.format(prestação))
if prestação <= minimo:
    print('\033[1;32;40mEmpréstimo pode ser CONCEDIDO\033[m')
else:
    print('\033[1;31;40mEmpréstimo NEGADO\033[m')
