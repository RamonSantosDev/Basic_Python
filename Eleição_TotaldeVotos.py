total = 0
total_eymael = 0
total_PadreKelmon = 0
total_cabo = 0
total_nulos = 0
total_branco = 0

print('Eleição presidencial\n1 - Eymael\n2 – Padre Kelmon\n3 - Cabo Daciolo\n'
      '4 – Voto nulo\n5 – Voto em branco ')
while True:
    voto = input('\nEscolhe seu Voto (ou "s" para sair): ')
    if voto != 's':
        total += 1
        if voto == '1':
            total_eymael += 1
        elif voto == '2':
            total_PadreKelmon += 1
        elif voto == '3':
            total_cabo += 1
        elif voto == '4':
            total_nulos += 1
        elif voto == '5':
            total_branco += 1
        else:
             print('Código de voto inválido.')
    else: # Saída do loop quando o usuário digita 's'
        break

# Cálculo das porcentagens
porcent_eymael = (total_eymael / total) * 100
porcent_PadreKelmon = (total_PadreKelmon / total) * 100
porcent_cabo = (total_cabo / total) * 100
porcent_nulos = (total_nulos / total) * 100
porcent_branco = (total_branco / total) * 100

# Impressão dos resultados
print('\nResultados da Eleição')
print('='*22)
print(f"Total de votos para Eymael: {total_eymael} - Porcentagem em %{porcent_eymael:.0f}")
print(f"Total de votos para Padre Kelmon: {total_PadreKelmon} - Porcentagem em %{porcent_PadreKelmon:.0f}")
print(f"Total de votos para Cabo Daciolo: {total_cabo} - Porcentagem em %{porcent_cabo:.0f}")
print(f"Total de votos Nulos: {total_nulos} - Porcentagem é %{porcent_nulos:.0f}")
print(f"Total de votos em Braco: {total_branco} - Porcentagem é %{porcent_branco:.0f}")

