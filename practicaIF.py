print("programa de evaluación de notas de alumnos")
notaAlumno = input()


def evaluacion(nota):
    valoracion = "aprobado" if nota >= 5 else "suspenso"
    return valoracion


print(evaluacion(notaAlumno))
