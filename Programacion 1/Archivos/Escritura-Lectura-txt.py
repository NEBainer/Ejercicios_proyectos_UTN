# archivo = open("Mi primer archivo", "w") #Al principio el nombre del archivo, segundo "W" que va a crear ese archivo si no existe, o sino lo sobreescribe. Si ponemos "A" va a apendicer el texte que introduzcamos, no lo va a sobreescribir como el "w"
# archivo.write("Hola, como estan?") #El texto que le agregamos a nuestro archivo
# print(archivo.name)
# archivo.close() #El profe recomienda siempre cerrar el archivo

# archivo = open("Mi primer archivo", "r")
# cadena = archivo.read()
# print(cadena)
# archivo.close()

lista = ["Mati", "Eze", "Maxi", "Doyel"]
with open("lista_nombres.txt", "W") as archivo:
    for nombre in lista:
        archivo.write(f"{nombre}\n")

with open("lista_nombres.txt", "r") as archivo:
    lista = archivo.readlines()

print((lista))

with open("lista_nombres.txt", "r") as archivo:
    for line in archivo:
        lista.append(line)
print(lista)