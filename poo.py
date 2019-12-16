class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()
        if (self.__enMarcha and chequeo):
            return "El Coche está en marcha"
        elif (self.__enMarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
              self.__largoChasis)

    def __chequeoInterno(self):
        print("realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("--------------------A contiuaación creamos el segundo objeto----------------------")
miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()
