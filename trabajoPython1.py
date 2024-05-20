vehiculo = "si"

print("¿Cuál es su edad?")
edad = float(input())

if edad > 17 and edad <= 25:
    print("¿Posee vehiculo propio (si o no)")
    vehiculo = input()
    if vehiculo == vehiculo:
        print("has pasado el primer proceso de seleción")
    else:
        print("No cumple con el requisito de vehiculo, espero una proxima oportunidad")
else:
    print("No cumple con el requisito de edad, espero una proxima oportunidad")
