def ingreseNota():
    while True:
        nota = float(input(f"Ingrese su nota {contador}:"))
        if nota >= 1 and nota <= 7:
            return nota
        else:
            print("Ingrese una nota entre 1 y 7")


sumaNotas = 0
contador = 1

while contador < 8:
    nota = ingreseNota()
    sumaNotas += nota
    contador += 1
print("El promedio del alumno es", sumaNotas / 7)
