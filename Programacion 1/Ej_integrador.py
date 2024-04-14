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

#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
contador_no_IA_no_fem = 0
contador_vueltas = 0

#Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género
contador_masculino = 0

for i in range(1,11):
    nombre = input("Ingrese su nombre: ")
    while nombre == None or nombre == "":
        nombre = input("Ingrese un nombre correcto: ")

    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 18:
        edad = input("La edad debe ser mayor a 18. Reingrese una edad valida: ")
        edad = int(edad)

    genero = input("Ingrese su genero: ")
    while genero == "" or genero == None or genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Ingrese un genero correcto: ")

    tecnologia = input("Ingrese la tecnologia a votar: ")
    while tecnologia == " " or tecnologia == None or tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Ingrese una tecnologia correcta: ")

    #Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
    if genero == "Masculino" and tecnologia != "RV/RA" and edad >= 25 and edad <= 50:
        contador_masculino_IOT_IA += 1

    #Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
    if (tecnologia != "IA" and genero != "Femenino") or edad >= 33 and edad <= 40:
        contador_no_IA_no_fem += 1

    #Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género
    if genero == "Masculino":
        contador_masculino += 1

    if contador_masculino == 1 or edad > edad_mayor_masculino:
        edad_mayor_masculino = edad
        nombre_mayor_masculino = nombre
        tecnologia_mayor_masculino = tecnologia

    contador_vueltas += 1

#Cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
if contador_masculino_IOT_IA > 0:
    mensaje = f"La cantidad de empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive es de:{contador_masculino_IOT_IA}\n"
else:
    mensaje = "No hubo empleados de genero masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive\n"

#Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
if contador_no_IA_no_fem > 0:
    porcentaje_no_IA_no_fem = (contador_no_IA_no_fem / contador_vueltas) * 100
    mensaje += f"El Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40 es de {porcentaje_no_IA_no_fem}%\n"
else:
    mensaje += "No hubo empleados que no votaron por IA, y que su genero no sea femenino o su edad se encuentre entre los 33 y 40 años\n"

#Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género
if contador_masculino > 0:
    mensaje += f"El Nombre de los empleados de género masculino con mayor edad es {nombre_mayor_masculino} y la tecnologia que voto fue {tecnologia_mayor_masculino}"
else:
    mensaje += "No hubo empleados del genero masculino"

print(mensaje)