from pro_orienta_objetos import *

#Funcion para mostrar ciertos atributos del personaje    
def mostrar_personaje(un_personaje: Personaje):
    print(f"{un_personaje.nombre} -- {un_personaje.nanotecnologia} -- {un_personaje.super_poder}")

#Ejemplo de uso del constructor
personaje_1 = Personaje(5, "IronMan", True, True, "Disparo Ultrasonico", 1000)

print(personaje_1.nombre)

print(personaje_1.super_poder)

mostrar_personaje(personaje_1)

presentacion = personaje_1.presentarse()

print(presentacion)

personaje_1.volar(1000, 200)

personaje_2 = Personaje(1, "BlackWidow", False, False, "Ataque cuerpo a cuerpo", 400)

print(personaje_2.presentarse()) 

print("\n")

personaje_2.atacar(personaje_1)

print(personaje_1.poder_pelea)
print(personaje_2.poder_pelea)