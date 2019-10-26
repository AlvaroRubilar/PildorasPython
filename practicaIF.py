print("programa de evaluación de notas de alumnos")
notaAlumno = input("Introduce la nota del alumno")


def evaluacion(nota):
    valoracion = "aprobado" if nota >= 5 else "suspenso"
    return valoracion


print(evaluacion(int(notaAlumno)))
