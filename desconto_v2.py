preco=float(input('Digite o valor da compra: '))

print("1.Á vista \n2.Á Vista Cartão \n3. Parcelado")
opcao = int(input("Escolha sua forma de pagamento: "))

if (opcao==1):
    calculo= preco * 0.90
    print(f'Preço final: {calculo}')
elif (opcao==2):
    calculo= preco * 0.95
    print(f'Preço final: {calculo}')
elif (opcao==3):
    print(f'Preço final: {preco}')
else:
    print('Opção inválida!')