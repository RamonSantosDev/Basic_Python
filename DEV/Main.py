class Main:
    pass



from Cliente import Cliente

from Conta import Conta

c1 = Cliente('Ramon', '114444-1212')
conta=Conta(c1.get_nome(), 15154)

conta.depositar(1200)
conta.saque(470)
conta.extrato()