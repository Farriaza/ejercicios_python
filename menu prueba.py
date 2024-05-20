import time  


# validacion de menu
def validaOpcion():
    try:
        opcion = int(input("Ingrese la opción requerida:"))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            print("ERROR..debe ingresar un valor de 1 a 3")
            return validaOpcion()
    except:
        print("ERROR..ingrese un valor valido")
        return validaOpcion()

#validacion submenu
def validaOpcion2():
    try:
        opcion = int(input("Ingrese la opción requerida: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("ERROR..debe ingresar un valor de 1 a 6")
            return validaOpcion2()
    except ValueError:
        print("ERROR..ingrese un valor valido")
        return validaOpcion2()


#lista ejercicio 1
def lista ():




#diccionario ejercicio 2
def mascotas():
    perro = {
        "nombre": "Manchas",
        "hambre": False,
        "sed": False,
        "aburrido": True,
        "peso": 8.3,
        "energía": 45,
        "vida": True,
        "foto": "(°^°)/",
    }

#opcion 1
def alimentar(perro):
    try:
        hambre = input(
            "¿Su mascota " + perro["nombre"] + " tiene hambre? (si / no): "
        ).lower()
        if hambre == "si":
            perro["hambre"] = False
            perro["peso"] += 1
            perro["energía"] += 0.5
            print("Se ha alimentado a", perro["nombre"])
        elif hambre == "no":
            print("La mascota", perro["nombre"], "no tiene hambre por el momento.")
        else:
            print("Por favor, ingrese solo 'si' o 'no'.")

    except ValueError:
        print("Por favor, ingrese solo 'si' o 'no'.")

#opcion2
def beber(perro):
    try:
        aburrido = input(
            "¿Su mascota " + perro["nombre"] + " está aburrido? (si / no): "
        ).lower()
        if aburrido == "si":
            perro["aburrido"] = False
            perro["energía"] -= 0.5
            perro["peso"] += 0.5
            print("Se ha jugado con", perro["nombre"])
        elif aburrido == "no":
            print("La mascota", perro["nombre"], "no está aburrida por el momento.")
        else:
            print("Por favor, ingrese solo 'si' o 'no'.")
    except ValueError:
        print("Por favor, ingrese solo 'si' o 'no'.")

#opcion 3
def estado(perro):
    print("Estado actual de", perro["nombre"])
    print("Hambre:", "Sí" if perro["hambre"] else "No")
    print("Sed:", "Sí" if perro["sed"] else "No")
    print("Aburrido:", "Sí" if perro["aburrido"] else "No")
    print("Peso:", perro["peso"], "kg")
    print("Energía:", perro["energía"])

    if perro["peso"] > 15:
        print(perro["nombre"], "tiene obesidad.")
    if perro["energía"] < 5:
        print(perro["nombre"], "tiene muy poca energía.")
    if perro["hambre"] and perro["sed"] and perro["aburrido"]:
        print(perro["nombre"], "puede que tenga alguna enfermedad.")
#opcion 4

def cambiaEstado(perro):
    perro["hambre"] = True
    perro["sed"] = True
    perro["aburrido"] = True
    print(
        "Estado de",
        perro["nombre"],
        "cambiado en su necesidades de hambre, sed y aburrido.",
    )


def mostrarMenu():
    print("====================================================")
    print("             Submenú mascota	                       ")
    print("====================================================")
    print("       1.- Alimentar                                ")
    print("       2.- Beber agua	                           ")
    print("       3.- Jugar	                                   ")
    print("       4.- Estado mascota                           ")
    print("       5.- Cambiar valores de la mascota            ")
    print("       6.- Volver al menu principal                 ")
    print("====================================================")


opcion = int(
    input(
        "Digite una opción del menú (1: Alimentar, 2: Jugar, 3: Ver estado, 4: Cambiar estado, 5: Salir): "
    )
)
while True:
    mostrarMenu()
    opcion = validaOpcion()
    if opcion == 1:
        mascotas(perro)
    elif opcion == 2:
        beber()
    elif opcion == 3:
        estado()

    elif opcion == 4:
        cambiaEstado()

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


def menu():  # Menu del aplicativo
    print("====================================================")
    print("   M E N Ú  P R I N C I P A L                       ")
    print("====================================================")
    print("       1.- Ingresar superhéroes a una lista o tupla ")
    print("       2.- Analizando a mi mascota                  ")
    print("       3.- Salir                                    ")
    print("====================================================")


while True:
    menu()
    opcion = validaOpcion()
    if opcion != 4:
        if opcion == 1:
            lista()

        elif opcion == 2:
            mascotas()

    else:
        print("Gracias por su visita, nos vemos.")
        time.sleep(5)
        break
