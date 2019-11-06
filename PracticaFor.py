email = False
miEmail = input("Introduce tu dirección de email: ")
for i in miEmail:
    if (i == "@"):
        email = True
print("El email es correcto"if email == True else "El email no es correcto")
