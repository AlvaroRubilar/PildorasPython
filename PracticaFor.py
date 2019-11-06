valido = False

email = input("Introduce tu email: ")
for i in range(len(email)):
        if email[i] == "@":
            valido = True
print("Email correcto" if valido else "Email incorrecto")
