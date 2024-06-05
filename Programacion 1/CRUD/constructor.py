'''CREATE'''
class Alumno: 
    def __init__(self, dni: int, nombre: str, apellido: str, nota: int):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    @staticmethod
    def ingresar_alumno_lista(lista_alumnos: list["Alumno"], un_alumno: "Alumno"):
        pass

'''READ'''
    @staticmethod
    def mostrar_todos_los_alumnos(lista_alumnos: list["Alumno"]):
        pass
    
    def mostrar_un_alumno(self):
        pass

'''UPDATE'''
    @staticmethod
    def modificar_alumno(lista_alumnos: list["Alumno"], dni: int):
        pass

'''DELETE'''
    @staticmethod
    def eliminar_alumno(lista_alumnos: list["Alumno"], dni: int):

'''PRUEBAS PARA UN POSIBLE MODULO MAIN'''
lista_alumnos:list[Alumno] = []
un_alumno = Alumno(20202020, "Pepe", "Ruiz", 7)
Alumno.ingresar_alumno_lista(lista_alumnos, un_alumno)
Alumno.mostrar_todos_los_alumnos(lista_alumnos)