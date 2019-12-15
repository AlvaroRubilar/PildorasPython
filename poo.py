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
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(True))
miCoche.estado()
print("--------------------A contiuaación creamos el segundo objeto----------------------")
miCoche2 = Coche()
print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene", miCoche2.ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.estado()
