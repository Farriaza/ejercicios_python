# menu
while True:
    print("                           Menú Principal")
    print("")
    print(
        "Dela siguientes opción digite el numero del comienzo de la siguiente oracion"
    )
    print("")
    print("1.- Para vocal y consonante")
    print("")
    print("2.- Para Palindromo")
    print("")
    print("3.- Para salir")
    print("")
    print("")
    print("ingrese su opción")
    opcion = float(input())

    # 1. Vocal o consonante

    if opcion == 1:

        def separarVocalesConsonantes(cadena):
            vocales = ""
            consonantes = ""

            for letra in cadena:
                if letra in "aeiou":
                    vocales += letra
                else:
                    consonantes += letra
            return vocales, consonantes

        palabra = input("ingrese una Letra y luego presiones ENTER:   ")
        vocalesResultado, consonantesResultados = separarVocalesConsonantes(palabra)
        print("Vocales:", vocalesResultado)
        print("")
        print("Consonantes:", consonantesResultados)
        print("")
        print("Ingrese otra opción del menú principal.")

    # Palíndromo

    if opcion == 2:

        def esPalindromo(palabra):
            palabra = palabra.lower().replace("", "")
            return palabra == palabra[::-1]

        palabra_ingresada = input("ingrese una palabra:")
        if esPalindromo(palabra_ingresada):
            print("La palabra es un palindromo.")
        else:
            print("La palabra no es un palindromo.")
        print("")
        print("Ingrese otra opción del menú principal.")

    # salida4

    if opcion == 3:
        print("usted a escogido la opción 3.")
        print("Hasta pronto.")
        break
    # opcion no valida
    if opcion != 1 and 2 and 3:
        print("solo opciones validas.")
        print("")
        print("Intente otra vez:")
