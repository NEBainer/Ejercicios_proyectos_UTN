class Personaje:
    #Atributos
    #Id - nombre - usa nano - vuela - super poder - Poder de pelea

    #Constructor(Nos permite inicializar los atributos de una clase con los valores que le ponemos entre parentesis)
    #Como el constructor es un metodo especial de una clase lo llamamos __init__ (Es algo definido de python)
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
            print(f"Estoy volando a una altura de {altura} metros y a una velocidad de {velocidad} km/h")
        else:
            print(f"{self.nombre}: Usted no sabe volar")

    def atacar(self, enemigo: "Personaje" ): #Tenemos que poner personaje por que o sino no sabemos de que esta hablando cuando le decimos enemigo. 
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"Gano: {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        elif self.poder_pelea < enemigo.poder_pelea:
            print(f"Gano: {enemigo.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print("Empataron")
