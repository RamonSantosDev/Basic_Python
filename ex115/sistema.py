from ex115.lib.interface import *
from ex115.lib.aquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do SISTEMA'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Cadatrar uma nova pessoa.
        cabeçalho('\033[4mNovo CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[1;7;31m Saindo do Sistema...Até logo \033[m')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida\033[m')
    sleep(1)