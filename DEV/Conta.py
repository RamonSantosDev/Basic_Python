class Conta:
    def __init__(self, titular, numero):
        self.saldo = 0.0
        self.numero = numero
        self.titular = titular


    def depositar(self, valor):
        self.saldo+=valor

    def saque(self, valor):
        if(self.saldo >= valor):
            self.saldo-=valor
            print('Saque realizado com Sucesso!')
        else:
            print('Saldo Insuficiente')

    def extrato(self):
        print(f"Cliente:{self.titular} / Saldo Atual:R${self.saldo}")


    def get_saldo(self):
        return self._saldo


    def set_saldo(self, saldo):
        if (saldo<0):
            print('O saldo não pode ser Negativo!')
        else:
            self._saldo = saldo