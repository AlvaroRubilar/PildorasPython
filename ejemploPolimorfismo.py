class Coche():
    def desplazamiento(self):
        print("Me deplazo utilizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplamentoVehiculo(vehiculo):
    vehiculo.desplazamiento()
miVehiculo = Moto()
desplamentoVehiculo(miVehiculo)
miVehiculo2 = Coche()
desplamentoVehiculo(miVehiculo2)
miVehiculo3 = Camion()
desplamentoVehiculo(miVehiculo3)
