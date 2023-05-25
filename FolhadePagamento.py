valor_hora = float(input('Valor de sua hora: '))
qntd_horas = float(input('Quantidades de Horas trabalhadas no mês: '))
salario_bruto = (valor_hora * qntd_horas)
if salario_bruto <= 900:
    IR = salario_bruto
    print('='*20)
    print('Isento')
    print('=' * 20)
elif salario_bruto <= 1500:
    IR = (salario_bruto * 5 / 100)
    print('=' * 20)
    print('Desconto de 5%')
    print('=' * 20)
elif salario_bruto <= 2500:
    IR = (salario_bruto * 10 / 100)
    print('\nDesconto de 10%')
elif salario_bruto > 2500:
    IR = (salario_bruto * 20 / 100)
    print('\nDesconto de 20%')

INSS = (salario_bruto * 10 / 100)
FGTS = (salario_bruto * 11 / 100)

salario_liq = salario_bruto - (IR + INSS)
desconto = salario_bruto - salario_liq

print('Salário Bruto: R$',salario_bruto)
print('(-)IR: R$',IR)
print('(-)INSS: R$',INSS)
print('FGTS: R$',FGTS)
print('Total de descontos: ',desconto)
print('Sálario Liquido: R$',salario_liq)
