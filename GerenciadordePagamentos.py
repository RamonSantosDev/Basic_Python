print('\033[1m{:=^22}\033[m'.format( ' Loja Ramon '))
valor = float(input('Valor do produto pago: '))
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal ')
print('[4] 3x ou mais no cartão: 20% de juros')
pagamento = int(input('Forma de Pagamento: '))
if pagamento == 1:
    valor = valor - (valor*10/100)
    print('O Senhor(a) teve 10% de desconto em sua compra, R${}'.format(valor))
elif pagamento == 2:
    valor = valor - (valor*5/100)
    print('O Senhor(a) teve 5% de desconto em sua compra, R${}'.format(valor))
elif pagamento == 3:
    total = valor
    parcela = total / 2
    print('O Senhor(a) vai que parcelar até 2x no cartão em sua compra, R${}'.format(parcela))
elif pagamento == 4:
    valor = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = valor / totalparc
    print('O Senhor(a) vai parcelar até {}x no cartão de R${:.2f} em sua compra COM JUROS, R${}'.format(totalparc, parcela, valor))
else:
    total = 0
    print('\033[1;31mOPÇÃO INVÁLIDA DE PAGAMENTO\033[m')