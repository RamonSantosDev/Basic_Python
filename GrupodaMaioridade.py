from datetime import date
totmaior = 0
totmenor = 0
print('\033[1mGrupo da Maioria\033[m')
for c in range(1,8):
    data = int(input('Em que ano a {}° pessoa nasceu: '.format(c))[:4])
    atual = date.today().year
    idade = atual - data
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Das 7 pessoas, {totmaior} são de maior',end=' ')
print(f'e {totmenor} são de menor')


