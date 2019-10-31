print("verificación de acceso")
edadUsuario = int(input("Introduce tu edad, por favor: "))
print("No puedes pasar" if 0 < edadUsuario < 18 else "Puedes pasar"if 0 <
      edadUsuario < 110 else "Edad incorrecta")
print("El programa ha finalizado")
