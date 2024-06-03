'''Un diccionario es una coleccion de elementos, donde cada uno tiene una key, que es unica, y un value'''
diccionario = {  #NO PUEDE HABER EN UN MISMO DICCIONARIO DOS VECES LA MISMA CLAVE CON EL MISMO NOMBRE
    'nombre': 'Juan',
    'edad': 21,
    'ciudad': 'Buenos Aires'
}
print(type(diccionario))
print(diccionario['nombre']) 
print(diccionario['edad'])
print(diccionario['ciudad'])
print(diccionario)

#Manera que tenemos para cambiar el valor dentro de una key de nuestro diccionario
diccionario['ciudad'] = "Cordoba"
print(diccionario['ciudad'])

edad = diccionario.pop("edad") #De esta manera eliminamos la key y el valor que tiene "edad" para adjuntar el valor que tiene a una variable 
print(edad)
print(diccionario)
'''En los arrays para obtener el indice de una palabra poniamos el numero de indice entre []. Con los diccionarios vamos a utilizar la primer letra de la clave. Por ejemplo para nombre vamos a utilizar 'n' '''

#Maneras de iterar un diccionario para que nos muestre su contenido
print(diccionario.keys()) #De esta manera vamos a recibir una lista con las claves.
print(diccionario.values()) #De esta manera vamos a recibir una lista con los valores.
print(diccionario.items()) #Asi nos devuelve todo junto

for clave in diccionario.keys():
    print(f"{clave} -> {diccionario[clave]}")

# for valor in diccionario.values():
#     print(valor)

for clave, valor in diccionario.items():
    print(f"{clave} -> {valor}")