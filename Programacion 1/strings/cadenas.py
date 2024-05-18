cadena = "Hola a todos"
print(cadena)
print(type(cadena))

caracter = cadena[3]
print(cadena) #Va a imprimir la "a" en Hola

cadena[0] = "L" #Nos va a tirar error. No podemos modificar un elemento de la cadena asi.

#Slicing: El primer numero es donde comienza(inclusive) y el segundo en donde termina
for i in range(0, 4):  #Manera que venimos utilizando
    print(cadena[i], end= "")

for i in range(5, len(cadena)):
    print(cadena[i], end = "")

print(cadena[3:6]) #El primer numero nos define el indice en donde queremos empezar inclusive, el segundo hasta donde. En este caso imprimira hasta la primer "a" hasta la "t" inclusive.
print(cadena[3:]) #3 hasta el final
print(cadena[:]) #Lo mismo que va a hacer si imprimimos solo cadena
print(cadena[:8]) #Va a imprimir todos desde la primer posicion hasta la posicion 8

nombre = input("Ingrese su nombre: ")
while len(nombre) > 10:
    nombe = input("Reingrese su nombre: ")


#Orden de los codigos ASCI
cadena_1 = "hola"
print(cadena == "hola")
print(cadena != "hola")
print(cadena == "Hola")
print(cadena < "hola")
print(cadena < "azul") #h = 104  a = 97
print(cadena > "azul") #h = 104  a = 97
print(cadena < "Perro") #h = 104  a = 97

#Ordenamiento alfabetico con burbujeo

nombres = ["Pepe", "Moni", "ana", "Coqui"]

for i in range (0, len(nombres) - 1):
    for j in range(i + 1, len(nombres)):
        if nombres[i] > nombres[j]:
            auxiliar = nombres[i]
            nombres[i] = nombres[j] 
            nombres[j] = auxiliar
print(nombres)

#Para que me imprima la cantidad de una letra en especifico
cadena = "Hola a todos"
contador_a = 0
for i in range(len(cadena)):
    if cadena[i] == "a":
        contador_a += 1

print(contador_a)

print(ord("H")) #Nos devuelve el numero ASCI del caracter

#Transforma todo en minuscula
cadena = "HoLa"
cadena_2 = ""
for i in range(len(cadena)):
    orden = ord(cadena[i])
    if orden>= 65 and orden <= 90:  #Es mayus
        cadena_2 += chr(orden+ 32)
        continue
    
    cadena_2 += cadena[i]

print(cadena_2)

#Lo mismo que arriba pero sin tener que validar en el rango
def buscar_caracter(busqueda, cadena):
    encontro = False
    for i in range(len(cadena)):
        if cadena[i] == busqueda:
            encontro = True
            break
    
    return encontro

caracteres_validos = "ABCDEFHIKP"

cadena = "HoLa"
cadena_2 = ""
for i in range(len(cadena)):
    caracter = cadena[i]
    if buscar_caracter(caracter, caracteres_validos):
        caracter = chr(ord(caracter) + 32)

    cadena_2 += caracter

print(cadena_2)