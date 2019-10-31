print("verificación de acceso")
edadUsuario = int(input("Introduce tu edad, por favor: "))
if edadUsuario < 18:
    print("No puedes pasar")
elif edadUsuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
print("El programa ha terminado")
