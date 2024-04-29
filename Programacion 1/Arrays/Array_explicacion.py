#Maneras incorrectas de mostrar una lista
#Maneras de crear una lista
mi_lista = []
mi_lista = list()
mi_lista = [0,1,2,31]
print(mi_lista)

#Manera de inicializar una lista con 5 elementos que empiezan en cero
mi_lista_2 = [0 ] * 5
print(mi_lista_2)

#Manera correcta de mostrar una lista
for i in range (len(mi_lista)):
    print(mi_lista[i])

for i in range (len(mi_lista_2)):
    print(mi_lista_2[i])

#Como mostrar un elemento en particular del array
print(mi_lista[3]) #En consola imprime el 31

#Como mostrar la cantidad de posiciones que tiene la lista
for i in range(len(mi_lista)):
    print(i) #Nos va a imprimir el indice de la lista(0,1,2,3)

#Mostrar los elementos de la lista con algun caracter de nuestra eleccion al final
for i in range(len(mi_lista)):
    print(mi_lista[i], end = " Oaaaaa ")