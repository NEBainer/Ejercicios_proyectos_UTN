class Boligrafo:
    def __init__(self, color, grosor):
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.color = color
        self.grosor = grosor

    def escribir(self, texto: str):
        grosor = 1
        if self.grosor == "Grueso":
            grosor = 2
        cantidad_tinta_utilizo = len(texto) * grosor
        if cantidad_tinta_utilizo > self.cantidad_tinta:
            mensaje ="No alcanza la tinta"         
        else:
            self.cantidad_tinta = self.cantidad_tinta - cantidad_tinta_utilizo
            mensaje = texto

        return mensaje
    
    def recargar(self, cantidad: int):
        self.cantidad_tinta = self.cantidad_tinta + cantidad
        mensaje = "Lapicera recargada"
        if self.capacidad_tinta_maxima < self.cantidad_tinta:
            exceso_tinta = self.cantidad_tinta - self.capacidad_tinta_maxima
            mensaje = f"Se recargó la lapicera y sobró {exceso_tinta} de cantidad de tinta."
            self.cantidad_tinta = self.capacidad_tinta_maxima
        
        return mensaje