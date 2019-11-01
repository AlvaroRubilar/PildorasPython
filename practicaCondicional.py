print("Asignaturas optativas año 2019")
print("Asinaturas Optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la escogida: ").lower()

print("Asignatura elegida " + asignatura.capitalize() if asignatura in ("Informática gráfica".lower(),"Pruebas de software".lower(), "Usabilidad y accesibilidad".lower()) else "La asignatura no está contemplada")