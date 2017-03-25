class Reloj:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def agregar_minuto(self):
        self.minutos += 1
        if self.minutos > 59:
            self.minutos = 0
            self.agregar_hora()

    def agregar_hora(self):
        self.horas += 1
        if self.horas > 23:
            self.horas = 0

    def __str__(self):
        return '{}:{}'.format(self.horas, self.minutos)

rolex = Reloj(10, 59)
rolex.agregar_minuto()
print(rolex)
rolex.agregar_hora()
print(rolex)
