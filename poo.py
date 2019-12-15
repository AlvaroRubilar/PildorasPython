class Coche():
    def __init__(self):
        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if (self.enMarcha):
            return "El Coche está en marcha"
        else:
            return "El Coche está parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
              self.largoChasis)


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()
print("--------------------A contiuaación creamos el segundo objeto----------------------")
miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()
