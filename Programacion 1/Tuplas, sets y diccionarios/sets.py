'''Los elementos de un set son unicos, no contienen elementos duplicados. 
No respetan el orden que tenian al ser declarados y sus elementos son inmutables'''

mi_set = {5,1,5,3,4} #Va a eliminar el numero repetido y lo va a ordenar como se le canta el culo. Mayormente te lo ordena de menor a mayor
print(mi_set)

#Los sets pueden ser utiles cuando en una lista tengo elementos repetidos
lista_sin_repetidos = list(mi_set)
print(mi_set)

#Puedo agregar elemento al set
mi_set.add("Pedrito")
print(mi_set)

#Tambien puedo eliminar elementos del set
mi_set.remove("Pedrito") #Lo malo con este metodo es que si no encuentra el elemento que le pasamos nos tira error
print(mi_set)
mi_set.discard(3) #METODO RECOMENDADO PARA ELEMINAR ELEMENTOS DE UN SET, YA QUE DE ESTA MANERA SI NO ENCUENTRA EL ELEMENTO NO TIRA ERROR
print(mi_set)

#Los sets son como los conjuntos, podemos hacer las mismas operaciones que con ellos con determinados metodos
set_a = {"Pipi", "Popo", "Pupu", "Pepe"}
set_b = {"Juanpi", "Juanca", "Pepe"}
set_resultado = set_a.union(set_b) #Une ambos sets
print(set_resultado)
set_resultado = set_a.intersection(set_b) #Muestra la intercepcion de ambos sets
print(set_resultado)
set_resultado = set_a.difference(set_b) #Muestra todo lo que esta en el set_a pero no en el b
print(set_resultado)