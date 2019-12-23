class Persona():
    def __init__(self, nombre, edad, lugarDeResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarDeResidencia = lugarDeResidencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugarDeResidencia)


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad


Antonio = Empleado(1500, 15, "Manuel", 55, "Colombia")
Antonio.descripcion()
