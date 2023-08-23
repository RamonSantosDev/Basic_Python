import time
import os


class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minitos = minutos
        self.horas = horas

    def __repr__(self):
        return f'{self.horas:02d}:{self.minitos:02d}:{self.segundos:02d}'

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minitos += 1
        if self.minitos >= 60:
            self.minitos = 0
            self.horas += 1

    def start(self):
        while True:
            os.system('cls')
            print(self)
            self.incremento()
            time.sleep(1)


cronometro1 = Cronometro()
cronometro1.start()
