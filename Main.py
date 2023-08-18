class Main:
    pass


print('Testando Projeto')
from Cliente import Cliente

from Conta import Conta

c1 = Cliente('Ramon', '114444-1212')
conta=Conta(c1.nome,15154,0)


print(f'{conta.titular} / Numero: {conta.numero} / Seu Saldo: {conta.saldo}')