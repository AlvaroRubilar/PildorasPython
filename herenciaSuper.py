class Persona():
    def __init__(self, nombre, edad, lugarDeResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarDeResidencia = lugarDeResidencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugarDeResidencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        self.salario = salario
        self.antiguedad = antiguedad


Antonio = Persona("Antonio", 55, "España")
Antonio.descripcion()
