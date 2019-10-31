print("verificación de acceso")
notaAlumno = float(input("Introduce tu nota, por favor: "))
if notaAlumno<5:
    print("Insuficiente")
elif notaAlumno<6:
    print("Suficiente")
elif notaAlumno<7:
    print("Bien")
elif notaAlumno<9:
    print("Notable")
else:
    print("Sobresaliente")
