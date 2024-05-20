import time  # utilizar libreria time, para realizar una pausa


# validacion de menu
def validaOpcion():
    try:
        opcion = int(input("Ingrese la opción requerida:"))
        if opcion >= 1 and opcion <= 4:
            return opcion
        else:
            print("ERROR..debe ingresar un valor de 1 a 4")
            return validaOpcion()
    except:
        print("ERROR..ingrese un valor valido")
        return validaOpcion()


# tupla
def numeroRango():
    while True:
        try:

            numero1 = int(input("\nNúmero inicial: "))
            numero2 = int(input("\nNúmero final: "))
            lista1 = []
            lista2 = []
            for numero in range(numero1, numero2 + 1):
                if numero % 2 == 0:
                    lista1.append(numero)
                else:
                    lista2.append(numero)

                lista1Tupla = tuple(lista1)
                lista2Tupla = tuple(lista2)
                pares = " / ".join(map(str, lista1Tupla))
                impares = " / ".join(map(str, lista2Tupla))

            return f"Los números pares son pares:\n{pares}\nLos números impares:\n{impares}"
        except:
            print("Error, tipo de datoi no vàlido. vuelva a intentar")


# diccionario
def valor():
    diccionario = {
        "10001-1": ["cemento melón", 2590, 140],
        "10202-1": ["ladrillo fiscal", 210, 9000],
        "10022-9": ["ladrillo princesa", 320, 4000],
        "10220-82": ["yeso", 890, 400],
    }
    print("\nDetalles de los productos y su valor venta final.")
    cementoMelon = diccionario["10001-1"][1] * diccionario["10001-1"][2]
    producto = diccionario["10001-1"][0].capitalize()
    print("\n", producto, "     =  ", "$", cementoMelon)

    ladrilloFiscal = diccionario["10202-1"][1] * diccionario["10202-1"][2]
    producto1 = diccionario["10202-1"][0].capitalize()
    print("", producto1, "   =  ", "$", ladrilloFiscal)

    ladrilloPrincesa = diccionario["10022-9"][1] * diccionario["10022-9"][2]
    producto3 = diccionario["10022-9"][0].capitalize()
    print("", producto3, " =  ", "$", ladrilloPrincesa)
    yeso = diccionario["10220-82"][1] * diccionario["10220-82"][2]
    producto4 = diccionario["10220-82"][0].capitalize()
    print("", producto4, "              =  ", "$", yeso)

    sumaTotal = (cementoMelon) + (ladrilloFiscal) + (ladrilloPrincesa) + (yeso)
    print("\nTotal en dinero a generar por ventas es de:", "$", sumaTotal)


# aplicativo
def aplicativo():

    def ingresarNumeros():
        numeros = []
        for valor in range(20):
            while True:
                try:
                    numero = int(input(f"Ingrese el número {valor + 1}: "))
                    if numero not in numeros:
                        numeros.append(numero)
                        break  # Salir del bucle si se ingresa un número válido
                    else:
                        print(
                            "Este número ya ha sido ingresado. Por favor, ingrese otro."
                        )
                except ValueError:
                    print("Por favor, ingrese solo números enteros.")
        return numeros

    def ordenarNumeros(numeros):
        numerosOrdenados = sorted(numeros)
        return numerosOrdenados

    def mostraresultados(numeros, numerosOrdenados):
        print("Números ingresados:")
        for numero in numeros:
            print(numero, end=" ")
        print("\nNúmeros ordenados de menor a mayor:")
        for numero in numerosOrdenados:
            print(numero, end=" ")

    def main():
        print("Ingrese 20 números enteros:")
        numeros = ingresarNumeros()
        numerosOrdenados = ordenarNumeros(numeros)
        mostraresultados(numeros, numerosOrdenados)

    if __name__ == "__main__":
        main()


def menu():  # Menu del aplicativo
    print("")
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- Tupla                ")
    print("       2.- Inventario           ")
    print("       3.- Lista                ")
    print("       4.- Salir                ")
    print("================================")
    print("")


while True:
    menu()
    opcion = validaOpcion()
    if opcion != 4:
        if opcion == 1:
            print(numeroRango())

        elif opcion == 2:
            valor()
        elif opcion == 3:
            aplicativo()
    else:
        print("Gracias por su visita, nos vemos.")
        time.sleep(5)
        break
