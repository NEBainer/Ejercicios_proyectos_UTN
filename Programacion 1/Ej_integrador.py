'''UTN TECHNOLOGIES Bainer Ezequiel

UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.'''

#Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
contador_masculino_IOT_IA = 0

for i in range(1,11):
    nombre = input("Ingrese su nombre: ")
    while nombre == None and nombre == "":
        nombre = input("Ingrese un nombre correcto: ")

    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("La edad debe ser mayor a 18. Reingrese una edad valida: ")
        edad = int(edad)

    genero = input("Ingrese su genero: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro" and genero == "" and genero == None:
        genero = input("Ingrese un genero correcto: ")

    tecnologia = input("Ingrese la tecnologia a votar: ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT" and tecnologia == " " and tecnologia == None:
        tecnologia = input("Ingrese una tecnologia correcta")

    #Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    if genero == "Masculino" and tecnologia != "RV/RA" and edad >= 25 and edad <= 50:
        contador_masculino_IOT_IA += 1

    #Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.


#Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
if contador_masculino_IOT_IA > 0:
    mensaje = f"La cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive es de:{contador_masculino_IOT_IA}\n"
else:
    mensaje = "No hubo empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive\n"
