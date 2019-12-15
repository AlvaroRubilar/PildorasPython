class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            return "El Coche está en marcha"
        else:
            return "El Coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
              self.__largoChasis)


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()
print("--------------------A contiuaación creamos el segundo objeto----------------------")
miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.__ruedas = 5
miCoche2.estado()
