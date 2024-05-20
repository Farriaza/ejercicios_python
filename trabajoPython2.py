calificacionesAlgebra = []

for nota in range(7):
    calificacion = float(input("Ingrese la calificación {}: ".format(nota + 1)))

    calificacionesAlgebra.append(calificacion)

promedio = sum(calificacionesAlgebra) / len(calificacionesAlgebra)

print("El promedio del alumno en Algebra es:", promedio)
