def calcular_troco(valor_mercadoria, valor_pago):
    troco = valor_pago - valor_mercadoria

    print('='*30)
    print(f'Valor da mercadoria: {valor_mercadoria}')
    print(f'Valor pago: {valor_pago}')
    print(f'Troco: {troco:.2f}')
    print('='*30,'\n')

    if troco < 0:
        print("Valor faltante: R$", abs(troco))
    elif troco == 0:
        print("Não existe troco!")
    else:
        notas_moedas = [5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
        troco_em_notas_moedas = []

        for nota_moeda in notas_moedas:
            quantidade = int(troco // nota_moeda)
            troco -= quantidade * nota_moeda
            troco_em_notas_moedas.append((quantidade, nota_moeda))

        for quantidade, nota_moeda in troco_em_notas_moedas:
            if quantidade > 0:
                if nota_moeda >= 1:
                    tipo = "Nota(s)"
                else:
                    tipo = "Moeda(s)"
                print(quantidade, tipo, "de R$", nota_moeda)
# Exemplo de uso:
valor_mercadoria = 250.70
valor_pago = 300.00
calcular_troco(valor_mercadoria, valor_pago)



