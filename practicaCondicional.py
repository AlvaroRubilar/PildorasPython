salarioPresidente = int(input("Introduce el salario del presidente "))
print("Salario presidente: "+str(salarioPresidente))

salarioDirector = int(input("Introduce el salario del director "))
print("Salario director: "+str(salarioDirector))

salarioJefeArea = int(input("Introduce el salario del jefe de área "))
print("Salario jefe de área: "+str(salarioJefeArea))

salarioAdministrativo = int(input("Introduce el salario del administrativo "))
print("Salario administrativo: "+str(salarioAdministrativo))

print("Todo funciona correctamente " if salarioAdministrativo < salarioJefeArea <
      salarioDirector < salarioPresidente else "Algo falla en la empresa")
