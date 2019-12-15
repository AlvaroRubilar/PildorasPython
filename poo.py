class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

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
