'''Para abrir un archivo'''
#archivo = open(nombre_archivo, modo)

#archivo -> objeto file, el cual sera utilizado para llamar a otros metodos asociados con el archivo
#nombre_archivo -> string que contiene el nombre del archivo al que queremos acceder
#modo -> string que contiene el modo de apertura del archivo

'''Para cerrar un archivo'''
#archivo.close()

'''Metodos para archivos'''
#archivo.closed -> retorna True si el archivo esta cerrado, sino, False.
#archivo.mode -> retorna el modo de acceso con el que el archivo ha sido abierto.
#archivo.name -> retorna el nombre del archivo.

# archivo = open("Mi segundo archivo", "w") #Al principio el nombre del archivo, segundo "W" que va a crear ese archivo si no existe, o sino lo sobreescribe. Si ponemos "A" va a apendicer el texte que introduzcamos, no lo va a sobreescribir como el "w". Si ponemos despues del nombre del archivo .txt(por ejemplo) especifica el tipo de archivo, tiene que ser antes del cierre de comillas.
# archivo.write("Buenasssss") #El texto que le agregamos a nuestro archivo
# # print(archivo.name)
# # archivo.close() #El profe recomienda siempre cerrar el archivo

# # archivo = open("Mi primer archivo", "r")
# # cadena = archivo.read()
# # print(cadena)
# # archivo.close()

'''Sentencia "with" para abrir archivos en python y dejar que el interprete se encargue de cerrar el mismo'''
lista = ["Mati", "Eze", "Maxi", "Doyel"]
with open("lista_nombres.txt", "w") as archivo:
    for nombre in lista:
        archivo.write(f"{nombre}\n")

# with open("lista_nombres.txt", "r") as archivo:
#     lista = archivo.readlines()

# print((lista))

# lista = []
# with open("lista_nombres.txt", "r") as archivo:
#     for line in archivo:
#         lista.append(line)
# print(lista)