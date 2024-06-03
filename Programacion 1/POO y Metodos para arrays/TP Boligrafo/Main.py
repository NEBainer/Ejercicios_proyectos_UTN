from Class_Boligrafo import *

boligrafo_1 = Boligrafo("Azul", "Fino")
boligrafo_2 = Boligrafo("Rojo", "Grueso")

#Probando el boligrafo 1
#Funcion de escribir(Ambos casos)
lapicera_1 = boligrafo_1.escribir("Perro")
print(lapicera_1)
lapicera_1 = boligrafo_1.escribir("De esta manera la dejamos sin tinta y despues la llenamos para comprobar como funciona recargar en ambos casos abajo")
print(lapicera_1)

#Funcion de recargar(Ambos casos)
lapicera_1 = boligrafo_1.recargar(2)
print(lapicera_1)
lapicera_1 = boligrafo_1.recargar(80)
print(lapicera_1)

#Probando el boligrafo 2
#Funcion de escribir(Ambos casos)
lapicera_2 = boligrafo_2.escribir("Perro")
print(lapicera_2)
lapicera_2 = boligrafo_2.escribir("Como tiene el doble de grosor nos quedamos sin tinta mas rapido")
print(lapicera_2)

#Funcion de recargar(Ambos casos)
lapicera_2 = boligrafo_2.recargar(2)
print(lapicera_2)
lapicera_2 = boligrafo_2.recargar(70)
print(lapicera_2)