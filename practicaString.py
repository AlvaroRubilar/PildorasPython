edad = input("Introduce tu edad: ")
while(edad.isdigit()==False):
    print("Por favor, introduce un valor numérico: ")
    edad = input("Introduce tu edad: ")
print("No puedes pasar" if int(edad) < 18 else "Puedes pasar")
