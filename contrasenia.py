# esto es para ver la opcion de contraseña basica
import sys

usuario = "usuario"
contrasenia = "1234"

for i in range(2):
    user = input("Dame un usuario: ")
    if user == usuario:
        for i in range(2):
            password = input("dame la contrasenia: ")
            if password == contrasenia:
                print("Bienvenido")
                sys.exit(0)
            else:
                print("Contraseña incorrecta")
    else:
        print("Usuario incorrecta")
