'''El CSV es un tipo de documento que representa los datos en forma de tabla, es decir, en filas y columnas. Las columnas son separadas, por un signo de puntuacion(,;.)u otro caracter y las diferentes filas suelen separarse por un salto de linea'''

nombres = ["Jose", "Maria", "Pedro"]
apellidos = ["Gomez", "Ruiz", "Perez"]
edades = [20, 45, 18]

# with open("agenda.csv", "w") as archivo:
#     for i in range(len(nombres)):
#         linea = f"{nombres[i]}, {apellidos[i]}, {edades[i]}\n"
#         archivo.write(linea)

with open("agenda.csv", "r") as archivo:
    for line in archivo:
        registro = line.split(",")
        print(f"{registro[0]} -- {registro[1]} -- {registro[2]}")