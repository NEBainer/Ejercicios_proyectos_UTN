'''JavaScrypt Object Notation.
Es un formato para el intercambio de datos basado en texto. Por lo que es facil de leer tanto para una persona como para una maquina.'''
import json

lista = []
lista.append({"nombre":"Luis", "edad":20})
lista.append({"nombre":"Maria", "edad":30})
lista.append({"nombre":"Pedro", "edad":18})

with open("personas.json", "w") as archivo:
    json.dump(lista, archivo, indent=4) #El indent crea 4 espacios para cada estructura

with open("personas.json", "r") as archivo: #Para ver el archivo en consola
    data = json.load(archivo)

print (data)