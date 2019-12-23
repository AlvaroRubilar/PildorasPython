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

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "\nAntigüedad", self.antiguedad)


Manuel = Persona( "Manuel", 55, "Colombia")
Manuel.descripcion()
print(isinstance(Manuel, Empleado))
