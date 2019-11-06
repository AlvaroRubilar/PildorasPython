contador = 0

miEmail = input("Introduce tu dirección de email: ")
for i in miEmail:
    if (i == "@" or i == "."):
        contador = contador + 1
print("El email es correcto"if contador >= 2 else "El email no es correcto")
