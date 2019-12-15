class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self):
        self.enMarcha = True
    def estado(self):
        if(self.enMarcha):
            return "El Coche está en marcha"
        else:
            return "El Coche está parado"


miCoche = Coche()
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, " ruedas")
miCoche.arrancar()
print(miCoche.estado())
