# tipos de datos

# 1 string : son textos
# 2 int : son numero enteros (2)
# flalt: son numero con coma o punto (4.5)
# booleanos:
# True : si esta condicion se cumple has esto...
# False: si no cumple has esto otro...

# variables: espacion que se almacena en la memoria del programa.(nombre es la variable)

# nombre = "Lucas Dalto" (nombre es la variable)
# print(nombre)
# las variables se declara con la escritura despues de =
# nombre es la variable pero "Lucas Dalto "  es la deficir la variable (darle un valor a la variable)

#   nombre = 10
#   nombre += 1

#   print(nombre)

# contatenacion: son cadenas de interaciones de la variable (nombre = nombre + " " + apellido)

# nombre = "Lucas"
# apellido = "Dalto"
# nombre = nombre + " " + apellido
# print(nombre)

# la funcion .format es para trasformar cualquier dato en palabras.

# ejemplo:  nombre= 5
# bienvenido = f"hola {nombre} ¿como estas?
# print(bienvenido)


# definir una variable
nombre = "Lucas"
nombreCompleto = "Lucas Dalto"  # calmelcase
nombre_completo = "Dalto Lukas"  # snake_case
# concatenar con *
bienvenido = "hola " + " ¿como estas?"

# concatenar con f-string
bienvenido = f"hola {nombre} ¿como estas?"

# operador de pertenencia(in / not in)
print("Lucas" in bienvenido)  # true
print("Lucas" not in bienvenido)  # false

# datos compuestos: son conjunto de datos

# lista
# lista = []
lista = ["Lucas", "Dalto", "soy Dalto"]
print(lista[0])
# tupla
# tupla = ()
tupla = ("lucas", "dalto", "soy Dalto")  # las tuplas no se puede modificar

# creando un conjunto (set):

conjunto = {"Lucas", "Dalto", "soy Dalto"}

# creando un diccionario

diccionario = {"nombre": "Lucas", "apellido": "Dalto", "edad": 31}

print(diccionario["apellido"])


# operadores aritmeticos

# suma y resta (+ y -)

suma = 12 + 5
resta = 12 - 5

# multiplicacion y division ( * y /)

multi = 12 * 5
division = 12 / 5

# potenciacion (exponente) (**)

exponente = 12**5

# division baja ( //)

division_baja = 12 // 5  # devuleve entero redoindea hacia abajo

# resto o modulo (%) nos muestra lo que sobra de la division

resto = 12 % 5

# tipos de datos(type)

typo_de_dato = type(resto)
print(suma)  # (en el parentesis se puede poner cualquier dato de las operacion )

# operadores de compracion

es_igual_que = 5 == 6
es_distinto = 5 != 6
es_menor_que = 5 < 6
es_menor_o_igual_que = 5 <= 6
es_mayor_que = 5 > 6
es_mayor_o_igual_que = 5 >= 6


# calculos combinados

a = 5
b = 10
c = 20

comparacion = a + b < c

print(comparacion)

# condicionales

edad = 18

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# otro ejemplo

ingreso_mensual = 50000
gastros_mensual = 2000

if ingreso_mensual > 10000:
    if ingreso_mensual - gastros_mensual > 1000:
        print("ahora si estas bien")
    else:
        print("ahora no")

elif ingreso_mensual >= 5000:
    print("Estas bien en Chile")

elif ingreso_mensual > 1000:
    print("Estas bien en Latino America")

else:
    print("busca mas ingresos")


# operadores logicos (or ,and,  not)

# and
resultado = True & True  # devolver True
resultado2 = False & True  # devolver Falso
resultado3 = True & False  # devolver Falso
resultado4 = False & False  # devolver Falso

# or
resultado5 = True & True  # devolver True
resultado6 = False & True  # devolver True
resultado7 = True & False  # devolver True
resultado8 = False & False  # devolver Falso

# not

resultado9 = not True  # devolver Falso
resultado10 = not False  # devolver True


print(resultado9)


# metodos

# cadena

cadena1 = "Hola soy Fernando dame 5"
cadena2 = "Bienvenido maquina"

resultado = cadena1.upper()  # convertir mayuscula
resultado2 = cadena1.lower()  # convierte en minusculas
resultado3 = cadena1.capitalize()  # convierte la primera letra en mayuscula
resultado4 = cadena1.find(
    "F"
)  # buscamos una cadena en otra cadena si no la encuentra muestra unn -1
resultado5 = cadena1.index(
    "5"
)  # buscamos una cadena en otra cadena si no la encuentra muestra un error
resultado6 = cadena1.isnumeric()  # buscamos una un numero en la cadena

resultado7 = (
    cadena1.isalpha()
)  # busca caracteres alfanumerico los espacios marcara un error

resultado8 = cadena1.count(
    " hola"
)  # busca la cantidad de caracteres que se repiten por ejemplo si seleccionamos la letra "a" en minuscula contara las veces que aparece la letra "a" lo mismo sucede su lo tomas como si fueran palabra "hola"

resultado10 = len(
    cadena1
)  # contamos las considencia dentro de las cadenas, devuelve la cantidad de concidencias

resultado11 = (
    cadena1.startswith()
)  # vereficamos si una cadena comienza (caracter) con otra cadena dada  , devuelve True

resultado11 = (
    cadena1.endswith()
)  # vereficamos si una cadena termina (carecter)con otra cadena dada  , devuelve True

resultado12 = cadena1.replace(
    "", ""
)  # si el valor 1, se encuentra en la cadena original, reemplazara el valor 1 de la misma

reultagdo13 = cadena1.split()  # separa la cadena con la cadena que  le pasemos

print(resultado)

# metodos de listas

lista = list(["hola", "fer", "31"])  # crear una lista

# devolver la cantidad de elemento en la lista

cantidad_elementos = len(lista)

lista.append("jajaja")

# aprepagndo un elemento de la lista en un indice especifico

lista.insert(2, "jajaja")

# agregando varios elementos a la lista

lista.extend(["Mono", 2023])

# eliminamos un elemento de la lista (por su indice)

lista.pop(
    2
)  # -1 para eliminar el ultimo, -2 para eliminar el penultimo y asi sucecivamente

# removiendo un elemento de la lista por su valor

lista.remove(2)

# ordenando la lista
lista.sort()  # lo ordena desendente

lista.sort(reverse=True)  # el "reverse" para ordenar de atars poara adelante

# invirtiendo los elmentos de una lista

lista.reverse()

# elimina todo la lista
lista.clear()


print(lista)
