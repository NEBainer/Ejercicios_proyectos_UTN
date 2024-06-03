
cadena = "hola      pepe        "
# SOLO SE USA PARA BORRAR LOS ESPACIOS DE ADELANTE Y ATRAS, FUNCIONA SOLO CON STR
cadena = cadena.strip()

# OTRO MODO DE USO // BORRA LA PALABRA QUE ESTA AL PRINCIPIO
cadena = cadena.strip("#")
cadena = cadena.strip("hola")
# SACA LOS ESPACIOS DEL PRINCIPIO Y DEL FINAL!
cadena = cadena.strip()

print(cadena)

### MANEJO DE CARACTERES ###
''' UPPER '''
# CONVIERTE EL STR EN MAYUSCULA #
cadena = "bRiAn"
cadena = cadena.upper()
# print(cadena)


''' LOWER '''
# CONVIERTE EL STR EN MINISCULA #
cadena = "bRiAn"
cadena = cadena.lower()
# print(cadena)


''' CAPITALIZE '''
# La primer letra de nuestro STR se convierte en Mayuscula, el resto va a ser miniscula #
cadena = "bRiAn"
cadena = cadena.capitalize()
# print(cadena)


''' REPLACE '''
# REMPLAZA EL PRIMER PARAMETRO POR EL SEGUNDO PARAMETRO DE LA FUNCION 
cadena = "Que inutil es esta funcion, no? GG'nt"
cadena = cadena.replace("GG","WIN")
print(cadena)


''' SPLIT '''   # MAS IMPORTANTE !!
# VA A BUSCAR EL PRIMER PARAMETRO, DSP DE ENCONTRARLO VA SER UTILIZADO COMO SEPARADOR ( EL STR SE CONVIERTE EN LISTA )
cadena = "matias*brian*jose*pedro*otros*nombres"
lista_nombres = cadena.split("*")
print(lista_nombres)
# NECESITO AGREGAR A ALGUIEN EN LA LISTA?
lista_nombres.append("carla") 
print(lista_nombres)


''' JOIN '''    # MAS IMPORTANTE !!
# VA A RECIBIR UNA LISTA, VA A DEVOLVER UN STR FORMATEADO DE LA MANERA QUE LE PEDIMOS.
cadena = "matias*brian*jose*pedro*otros*nombres"

separador = "#"
cadena = separador.join(lista_nombres)
cadena = "&".join(lista_nombres)
# print(cadena)


''' ZFILL '''
# RELLENA LA CADENA CON CEROS A LA IZQUIERDA HASTA LLEGAR A LA LONGITUD PASADA COMO PARAMETRO
hora = "01:01"

# print(hora)
hora = hora.zfill(15)
# print(hora)


''' ISALPHA '''
# Verifica si todos los caracteres son ALPHANUMERICS, Return Bool
cadena = "Brian"

print(cadena)

booleano = cadena.isalpha()

print(booleano)


''' COUNT '''
# Devuelve la cantidad de coincidencias del argumento con la variable
cadena = "brian brian brian brian"

# print(cadena)

cantidad = cadena.count("brian")

# print(cantidad)


''' FORMAT '''
#
nombre = "Brian"
apellido = "Bocca"

na = "Nombre: {0} --- Apellido: {1}"
# print(na.format(nombre,apellido))


''' FIND '''
# INVESTIGAR ...


''' SLICE '''
# CORTA LA VARIABLE
cadena = "Brian bocca"
# INCLUYE EL PRIMER ARGUMENTO, EXCLUYE EL SEGUNDO
nombre = cadena[0:5]
nombre = nombre.capitalize()
# SI NO PONEMOS EL PARAMETRO OPUESTO, ES EL INICIO O EL FINAL =  " :4 "
apellido = cadena[6:]
apellido = apellido.capitalize()

cadena = nombre + " " + apellido

print(cadena)