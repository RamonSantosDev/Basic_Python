def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mValor inválido! Digite um número inteiro válido.\033[m")
            #[Continue], serve para retornar novamente a [msg] no [while]
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mÚsuario preferiu não informar os dados\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[1;30m-\033[m' * tam


def cabeçalho(txt):
    print(linha())
    print(f'\033[1m{txt.center(40)}\033[m')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1m{c} -\033[m \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1mSua Opção: \033[m')
    return opc