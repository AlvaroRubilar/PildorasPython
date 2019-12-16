class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "voy haciendo el caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
