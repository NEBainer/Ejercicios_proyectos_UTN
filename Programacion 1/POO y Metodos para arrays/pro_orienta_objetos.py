class Personaje:
    #Atributos
    #Id - nombre - usa nano - vuela - super poder

    #Constructor(Nos permite inicializar los atributos de una clase con los valores que le ponemos entre parentesis)

    def __init__(self, id, nombre, nano, vuela, super_poder, poder_pelea):     #Con self agarramos el objeto y le ponemos los atributos que tenemos en el molde
        self.id = id
        self.nombre = nombre
        self.nanotecnologia = nano
        self.vuela = vuela
        self.super_poder = super_poder
        self.poder_pelea = poder_pelea


    #Metodos: Volar - Correr - Atacar
    def presentarse(self):
        cadena = f"{self.nombre} - {self.super_poder}"
        if self.nanotecnologia:
            cadena += f" - Usa Nanotecnologia"
        else:
            cadena += f" - No usa Nanotecnologia"

        return cadena

    def volar(self, altura, velocidad):
        if self.vuela:
            print(f"Estoy volando a una altura de {altura} y a una velocidad de {velocidad} km/h")
        else:
            print(f"{self.nombre}: Usted no sabe volar")

def mostrar_personaje(un_personaje: Personaje):
    print(f"{un_personaje.nombre} -- {un_personaje.nanotecnologia} -- {un_personaje.super_poder}")

#Ejemplo de uso del constructor
personaje_1 = Personaje(5, "IronMan", True, True, "Disparo ultrasonico", 1000)

mostrar_personaje(personaje_1)