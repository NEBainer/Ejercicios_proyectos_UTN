''' Se ha encontrado una muestra de ADN en el lugar del crimen que contiene la siguiente secuencia de bases nitrogenadas: “CGTTTAATG”. La investigación ha revelado tres posibles sospechosos, cada uno con su propia muestra de ADN:
Juan Pérez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
María Rodríguez
Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
Carlos Sánchez
Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

Para resolver el caso, nos piden que desarrollemos un programa que compare las combinaciones de bases nitrogenadas de la muestra encontrada con las muestras de los sospechosos. 
Mostrar el nombre por pantalla en caso de encontrar al asesino, o la leyenda “SON TODOS INOCENTES”. 
'''
def comparar_muestras(nombre: str, muestra: str) -> bool:
    evidencia = "CGTTTAATG"
    longitud_de_muestra = len(muestra)
    longitud_de_evidencia = len(evidencia)

    for i in range(longitud_de_muestra - longitud_de_evidencia + 1):
        if muestra[i:i + longitud_de_evidencia] == evidencia:
            return True
    
    return False

def comprobar_inocencia(valor: bool, nombre: str) -> str:
    if valor == False:
        mensaje = "El sospechoso ingresado es inocente :D"
    else:
        mensaje = f"El asesino es {nombre}!!!"
    return mensaje


caso_1 = caso_2 = caso_3 = False
bandera_seguir = False
while bandera_seguir == False:
    sospechoso = input("Ingrese el nombre del sospechoso al cual se le analizara la base nitrogenada: ")
    while sospechoso != "Juan" and sospechoso != "María" and sospechoso != "Carlos":
        sospechoso = input("Ingrese el nombre correcto del sospechoso: ")

    match sospechoso:
        case "Juan":
            muestra_adn_1 = "CGGGGCTAAAATTTTTTACGATCG"
            nombre_1 = "Juan Pérez"
            caso_1 = comparar_muestras(nombre_1, muestra_adn_1)
            resultado = comprobar_inocencia(caso_1, nombre_1)
            print(resultado)
            bandera_seguir = caso_1
        case "María":
            muestra_adn_2 = "AACGTTTAATGTTCTAAGCTGCG"
            nombre_2 = "María Rodríguez"
            caso_2 = comparar_muestras(nombre_2, muestra_adn_2)
            resultado = comprobar_inocencia(caso_2, nombre_2)
            print(resultado)
            bandera_seguir = caso_2
        case "Carlos":
            muestra_adn_3 = "CGGGGCTAAAATTTTTTACGATCG"
            nombre_3 = "Carlos Sánchez"
            caso_3 = comparar_muestras(nombre_3, muestra_adn_3)
            resultado = comprobar_inocencia(caso_3, nombre_3)
            print(resultado)
            bandera_seguir = caso_3
    
    