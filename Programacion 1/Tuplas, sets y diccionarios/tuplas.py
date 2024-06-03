'''Las tuplas son inmutables, no podemos agregarles elementos ni sacarles'''
lista = tuple([1, "Hola", 3.67])
print(type(lista))
print(lista[1])
# lista[1] = "Chau" Esto nos tiraria error ya que estamos intentando modificar un elemento de la tupla

#Otra manera de crear una tupla
tupla = (4, "a", 54)

#Podemos asignar los elementos de una tupla a una variable
a, b, c = tupla

print(a)
print(b)
print(c)

#Otra manera de asignar los elementos de una tupla
def hacer(punto):
    x = punto[0]
    y = punto[1]
    x, y = punto

a = 45 # Asi podemos modificar esa variable, de todas maneras la tupla no se va a modificar

#Si tenemos un array dentro de una tupla, podemos modificar los elementos de ese array :O
tupla =(4, 3, [4,7,2])
a, b, c = tupla
c.sort()
print(tupla)

#Metodos que le podemos aplicar a la tupla(count, index)
tupla2 = (4,3,2,4)
print(tupla2.count(4))
print(tupla2.index(4))