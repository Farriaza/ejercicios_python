# esto es para calcular porcentajes
print("Ingrese el monto neto :")
numero = float(input())
print("Ingrese el % que desea calcular")
porcentaje = float(input())
print("ingrese el % que desea descontar del liquido")
numero2 = float(input())
resultado = numero * 0.19

liquido = resultado + numero
descuento = liquido * numero2 / 100
resultado2 = liquido - descuento
print("El", round(porcentaje), " porciento de ", round(numero), "es", round(resultado))
print("Total liquido es de ", round(liquido))
print("El descuento es de ", round(descuento))
print("Total a pagar es de ", round(resultado2))
