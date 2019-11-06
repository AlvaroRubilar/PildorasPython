email = False
for i in "juan@pildorasinformaticas.es":
    if (i == "@"):
        email = True
print("El email es correcto"if email == True else "El email no es correcto")
