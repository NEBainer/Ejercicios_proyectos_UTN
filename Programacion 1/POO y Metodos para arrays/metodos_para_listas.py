#Metodo append: Agrega un elemento al final de la lista
mi_lista = [1,2,3]

mi_lista.append(1) #Le podes pasar lo que te pinte y guarda el elemento que le pasas como parametro al final de la lista

print(mi_lista)

#Insert: Inserta un elemento en la posicion especifica
mi_lista.insert(1, 5 ) #En el primer lugar va la posicion del elemento a reemplazar, en el segundo colocamos el valor que va a colocar en ese lugar

print(mi_lista)

#Remove: Elimina la primera ocurrencia del elemento especificado
mi_lista.remove(1)

print(mi_lista)

#Metodo con el remove para ir eleminando un elemento en especifico dentro de una lista
lista = [1,2,4,2,5,2]

for numero in lista:
    if numero == 2:
        lista.remove(numero)

#Pop: Elimina y devuelve el elemento en la posicion dada. Si no se especifica un indice, se elimina y devuelve el ultimo elemento
elemento = mi_lista.pop(1) #Guarda el elemento que borramos con el pop en la variable
print(mi_lista) 
mi_lista.append(elemento) #Volvemos a agregar el 2

print(elemento)
print(mi_lista)

#Index: Devuelve el indice de la primera ocurrencia del elemento especificado
mi_lista2 = [7,9,5]
indice = mi_lista2.index(7)
print(indice)

#Sort: Ordena la lista
mi_lista2.sort()
print(mi_lista2)

#Reverse: Invierte la lista
mi_lista2.reverse()
print(mi_lista2)

#Clear: Vacia la lista
mi_lista2.clear()
print(mi_lista2)