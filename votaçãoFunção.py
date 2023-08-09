def voto(nascimento):
    from datetime import date
    idadeUsuario = date.today().year - nascimento
    if idadeUsuario < 16:
        return f'com {idadeUsuario} anos: NÃO VOTA.'
    elif 18 <= idadeUsuario <= 75:
        return f'com {idadeUsuario} anos: VOTO OBRIGATÓRIO.'
    else:
        if idadeUsuario > 75:
            return f'com {idadeUsuario} anos: VOTO OPCIONAL.'

while True:
    print('-' * 30)
    usuarioNome = str(input('Digite seu nome: ')).capitalize()
    usuarioNascimento = int(input('Em que ano você nasceu? '))

    print(f'{usuarioNome} está ',end='')
    print(f'{voto(usuarioNascimento)}')
    resp = str(input('Deseja Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nENCERRADO')