class Persona():
    def __init__(self, nombre, edad, lugarDeResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarDeResidencia = lugarDeResidencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugarDeResidencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        super().__init__("Antonio", 55, "España")
        self.salario = salario
        self.antiguedad = antiguedad


Antonio = Empleado(1500, 15)
Antonio.descripcion()
