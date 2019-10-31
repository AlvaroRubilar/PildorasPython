print("Programa de becas año 2019")

distanciaEscuela = int(input("Introduce la distancia a la escuela en km "))
print(distanciaEscuela)

numeroHermanos = int(input("Introduce el n° de hermanos en el centro "))
print(numeroHermanos)

salarioFamiliar = int(input("Introduce salario anual en bruto "))
print(salarioFamiliar)

print("Tienes derecho a beca" if distanciaEscuela > 40 and numeroHermanos >
      2 and salarioFamiliar <= 20000 else "No tienes derecho a beca")
