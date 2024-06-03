"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberan listar todos los temas lanzados en ese mes sin importar el año
I. SALIR

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
from os import system
from data import lista_videos
from class_video import Video

bandera_ingreso = False
bandera_seguir = True
while bandera_seguir == True:
    menu_de_opciones = input( "A. NORMALIZAR OBJETOS. \nB. MOSTRAR TEMAS. \nC. ORDENAR TEMAS. \nD. PROMEDIO DE VISTAS. \nE. MAXIMA REPRODUCCION. \nF. BUSQUEDA POR CODIGO. \nG. LISTAR POR COLABORADOR. \nH. LISTAR POR MES. \nI. SALIR. \n")

    match menu_de_opciones:
        case "A":
            bandera_ingreso = True
            for video in lista_videos:
                video.dividir_titulo()
                video.obtener_codigo_url()
                video.formatear_fecha()
        case "B":
            if bandera_ingreso == True:
                for video in lista_videos:
                    video.mostrar_tema()
            else:
                print("Ingrese primero a la opcion A para normalizar los videos.")
        case "C":
            if bandera_ingreso == True:
                for video in lista_videos:
                    video.ordenar_temas()
            else:
                print("Ingrese primero a la opcion A para normalizar los videos.")
        case "D":
            if bandera_ingreso == True:
                promedio_vistas = Video.promediar_vistas(lista_videos)
                print(promedio_vistas)
            else:
                print("Ingrese primero a la opcion A para normalizar los videos.")
        # case "E":
        #     if bandera_ingreso == True:
            
        #     else:
        #         print("Ingrese primero a la opcion A para normalizar los videos.")
        # case "F":
        #     if bandera_ingreso == True:
            
        #     else:
        #         print("Ingrese primero a la opcion A para normalizar los videos.")
        # case "G":
        #     if bandera_ingreso == True:
            
        #     else:
        #         print("Ingrese primero a la opcion A para normalizar los videos.")

        # case "H":
        #     if bandera_ingreso == True:
            
        #     else:
        #         print("Ingrese primero a la opcion A para normalizar los videos.")

        case "I":
            print("Saliendo del programa...")
            bandera_seguir = False

    system("pause")
    system("cls")
