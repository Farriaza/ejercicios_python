import time  # utilizar libreria time, para realizar una pausa


def validaOpcion():
    try:
        opcion = int(input("\nIngrese la opción requerida:"))
        if opcion >= 1 and opcion <= 4:
            return opcion
        else:
            print("\nERROR..debe ingresar un valor de 1 a 4")
            return validaOpcion()
    except:
        print("\nERROR..ingrese un valor valido")
        return validaOpcion()


def semanal():

    listaDias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo",
    ]

    def validarNumeroDia(numero):
        return numero.isdigit()  # Verifica si la cadena contiene solo dígitos

    while True:
        numeroDia = input("\nIngrese el número del día (1-7): ")
        if validarNumeroDia(numeroDia):
            if 1 <= int(numeroDia) <= 7:
                break
            else:
                print("\nPor favor, ingrese un número de día válido (entre 1 y 7).")
        else:
            print("\nPor favor, ingrese solo números.")

    indiceDia = int(numeroDia) - 1
    print("\nEl día correspondiente es:", listaDias[indiceDia])
    print("\nSelecciones otra opción del menú:")


def azar():

    import random

    numero = int(input("\nIngrese la cantidad de números enteros a generar: "))

    tuplaNumeros = tuple(random.randint(1, 10) for _ in range(numero))

    numeroBuscar = int(input("\nIngrese un número para buscar en la tupla (1-10): "))

    conteo = tuplaNumeros.count(numeroBuscar)

    print(f"\nEl número {numeroBuscar} aparece {conteo} veces en la tupla.")
    print("\nPara su seguridad la tupla creada fue:", tuplaNumeros)
    print("\nSelecciones otra opción del menú:")


def frutas():
    diccionario = {
        "manzanas": 1200,
        "platanos": 1400,
        "uvas": 2000,
        "naranjas": 850,
        "peras": 1000,
        "tunas": 1300,
    }

    listaFrutas = ["manzanas", "platanos", "uvas", "naranjas", "peras", "tunas"]

    compras = []
    totalCompra = 0

    while True:
        print(
            "\nTenemos las siguientes frutas a la venta: manzanas, platanos, uvas, naranjas, peras, tunas"
        )

        while True:
            fruta = input("\n¿Cuál desea comprar?: ").lower()

            if fruta not in listaFrutas:
                print(
                    "\nLo siento, esa fruta no está disponible. Por favor, seleccione una de las opciones disponibles."
                )

            else:
                print("\nHas seleccionado", fruta)
                break

        busqueda = fruta

        print(
            "\nLa fruta seleccionada tiene un valor de $",
            diccionario[fruta],
            "por kilo.",
        )

        while True:
            try:
                precio = int(input("\n¿Cuántos kilos desea?: "))
                break
            except ValueError:
                print("\nPor favor, ingrese solo números enteros.")

        valorTotal = diccionario[fruta] * precio

        print(
            "Usted seleccionó",
            busqueda,
            ", que tiene un valor por kilo de: $",
            diccionario[fruta],
            ",Usted lleva",
            precio,
            "kilos, que nos da un total a pagar de : $",
            valorTotal,
        )

        compras.append(
            {
                "fruta": busqueda,
                "precioPorkilo": diccionario[fruta],
                "kilos": precio,
                "total": valorTotal,
            }
        )

        totalCompra += valorTotal

        while True:
            continuar = input("¿Desea realizar otra compra? (si/no): ").lower()
            if continuar == "si":
                break
            elif continuar == "no":
                print("\nResumen de compras:")
                for compra in compras:
                    print(
                        f"{compra['fruta']}: {compra['kilos']} kg - ${compra['total']}"
                    )
                print(f"\nTotal de la compra: ${totalCompra}")
                print("\nGracias por su compra. ¡Hasta luego!")
                print("\nSelecciones otra opción del menú:")
                return
            else:
                print("Por favor, ingrese 'si' o 'no'.")


def menu():
    print("")
    print("+" + "-" * 60 + "+")
    print("|" + " " * 20 + " Menú Principal " + " " * 24 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + " " * 12 + "1. Determinar el día en palabras" + " " * 16 + "|")
    print("|" + " " * 12 + "2. Frecuencia de un número" + " " * 22 + "|")
    print("|" + " " * 12 + "3. Venta de frutas" + " " * 30 + "|")
    print("|" + " " * 12 + "4. Salir" + " " * 40 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")


while True:
    menu()
    opcion = validaOpcion()
    if opcion != 4:
        if opcion == 1:
            semanal()

        elif opcion == 2:
            azar()

        elif opcion == 3:
            frutas()

        time.sleep(2)

    else:
        print("\nGrascias por su compra, nos vemos pronto")
        time.sleep(5)
        break
