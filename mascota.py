import time


# Validación menú principal
def validaOpcion():
    try:
        opcion = input("Ingrese la opción requerida:")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 3:
                return opcion
            else:
                print("ERROR: Debe ingresar un valor entre 1 y 3")
                return validaOpcion()
        else:
            print("ERROR: Debe ingresar un número")
            return validaOpcion()
    except ValueError:
        print("ERROR: Ingrese un valor válido")
        return validaOpcion()


# super heroes
def sumasuper():
    listasuper = []

    while True:
        try:
            superheroe = (
                input("\nIngrese el nombre de un Superhéroe o 'FIN' para terminar: ")
                .strip()
                .upper()
            )

            if not superheroe:
                print(
                    "\nDebes ingresar el nombre de un Superhéroe o 'FIN' para terminar."
                )
                continue

            elif superheroe == "FIN":
                if listasuper:
                    print("Lista de Superhéroes:")
                    print(" / ".join(listasuper))
                else:
                    print("No se han ingresado superhéroes.")
                print("\nGracias por ayudarnos a crear esta lista.")
                break

            elif superheroe == "M":
                if listasuper:
                    print("\nLista de Superhéroes:")
                    print(" / ".join(listasuper))
                else:
                    print("\1No se han ingresado superhéroes aún.")
                continue

            elif superheroe in listasuper:
                print("\n¡Superhéroe repetido! Intenta ingresar otro.")
                continue

            elif not superheroe.isalpha():
                raise ValueError(
                    "\nSi el super heroes tiene dos o mas palabras puedes escribirlas con la  segunda palabra comenzar con mayuscula ejemplo : superMAn."
                )

            else:
                listasuper.append(superheroe)

        except ValueError as e:
            print("Error:", e)

    return listasuper


# submenú validacion
def validaOpcion2():
    try:
        opcion = input("Ingrese la opción requerida:")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("ERROR: Debe ingresar un valor entre 1 y 6")
                return validaOpcion2()
        else:
            print("ERROR: Debe ingresar un número")
            return validaOpcion2()
    except ValueError:
        print("ERROR: Ingrese un valor válido")
        return validaOpcion2()


# submenu
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
    while True:
        print("====================================================")
        print("             Submenú mascota                        ")
        print("====================================================")
        print("       1.- Alimentar                                ")
        print("       2.- Beber agua	                           ")
        print("       3.- Jugar	                                   ")
        print("       4.- Estado mascota                           ")
        print("       5.- Cambiar valores de la mascota            ")
        print("       6.- Volver al menu principal                 ")
        print("====================================================")

        opcion = validaOpcion2()

        if opcion == 1:
            alimentar(perro)
        elif opcion == 2:
            beber(perro)
        elif opcion == 3:
            jugar(perro)
        elif opcion == 4:
            estado(perro)
        elif opcion == 5:
            cambiaEstado(perro)
        elif opcion == 6:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")


# alimento
def alimentar(perro):
    while True:
        try:
            hambre = input(
                "\n¿Su mascota " + perro["nombre"] + " tiene hambre? (si / no): "
            ).lower()
            if hambre == "si":
                perro["hambre"] = False
                perro["peso"] += 1
                perro["energía"] += 0.5
                print("Se ha alimentado a", perro["nombre"])
            elif hambre == "no":
                print(
                    "\nLa mascota", perro["nombre"], "no tiene hambre por el momento."
                )
            else:
                print("\nPor favor, ingrese solo 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("\nPor favor, ingrese solo 'si' o 'no'.")


# beber
def beber(perro):
    while True:
        try:
            sed = input(
                "\n¿Su mascota " + perro["nombre"] + " tiene sed? (si / no): "
            ).lower()
            if sed == "si":
                perro["sed"] = False
                perro["energía"] += 0.3
                print("\nSe ha dado agua a", perro["nombre"])
            elif sed == "no":
                print("\nLa mascota", perro["nombre"], "no tiene sed en este momento.")
            else:
                print("\nPor favor, ingrese solo 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("\nPor favor, ingrese solo 'si' o 'no'.")


# jugar
def jugar(perro):
    while True:
        try:
            aburrido = input(
                "¿Su mascota " + perro["nombre"] + " está aburrido? (si / no): "
            ).lower()
            if aburrido == "si":
                perro["aburrido"] = False
                perro["energía"] -= 0.5
                perro["peso"] += 0.5
                print("\nSe ha jugado con", perro["nombre"])
            elif aburrido == "no":
                print(
                    "\nLa mascota", perro["nombre"], "no está aburrida en este momento."
                )
            else:
                print("\nPor favor, ingrese solo 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("\nPor favor, ingrese solo 'si' o 'no'.")


# estado
def estado(perro):
    print("\nEstado actual de", perro["nombre"])
    print("\nHambre:", "Sí" if perro["hambre"] else "No")
    print("\nSed:", "Sí" if perro["sed"] else "No")
    print("\nAburrido:", "Sí" if perro["aburrido"] else "No")
    print("\nPeso:", perro["peso"], "kg")
    print("\nEnergía:", perro["energía"])

    if perro["peso"] > 15:
        print(perro["nombre"], "tiene obesidad.")
    if perro["energía"] < 5:
        print(perro["nombre"], "tiene muy poca energía.")
    if perro["hambre"] and perro["sed"] and perro["aburrido"]:
        print(perro["nombre"], "puede que tenga alguna enfermedad.")


# cambio de estado
def cambiaEstado(perro):
    perro["hambre"] = True
    perro["sed"] = True
    perro["aburrido"] = True
    print(
        "\nEl estado de",
        perro["nombre"],
        "a cambiado en sus necesidades de hambre, sed y aburrimiento.",
    )


# menúprincipal
def menu():
    print("====================================================")
    print("   M E N Ú  P R I N C I P A L                       ")
    print("====================================================")
    print("       1.- Ingresar superhéroes a una lista o tupla ")
    print("       2.- Analizando a mi mascota                  ")
    print("       3.- Salir                                    ")
    print("====================================================")


# opciones  menú principal
while True:
    menu()
    opcion = validaOpcion()
    if opcion == 1:
        sumasuper()
    elif opcion == 2:
        mascotas()
    elif opcion == 3:
        print("\nGracias por su visita, nos vemos.")
        time.sleep(5)
        break
