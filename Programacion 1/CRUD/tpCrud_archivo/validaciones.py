def validar_nombre(nombre: str) -> str:
    while not (nombre.isalpha() and len(nombre) <= 20):
        nombre = input("Nombre invalido. Asegurese que solo contenga letras y no supere los 20 caracteres.\n")
    return nombre

def validar_dni(dni: str) -> int:
    while not (dni.isdigit() and 5000000 <= int(dni) <= 99999999):
        dni = input("DNI inválido. Debe ser un valor numérico entre 5000000 y 99999999:\n")
    return int(dni)

def validar_puesto(puesto: str) -> str: 
    while puesto != "Gerente" and puesto != "Supervisor" and puesto != "Analista" and puesto != "Encargado" and puesto != "Asistente": 
        puesto = input("Puesto ingresado incorrecto. Ingrese uno de los siguientes puestos: “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”\n")
    return puesto

def validar_salario(salario: str) -> int:
    while not (salario.isdigit() and int(salario) > 234315):
        salario = input("Salario inválido. Debe ser un valor numérico mayor a 234315:\n")
    return int(salario)

def modificar_otro_dato() -> bool:
    consultar = input("Desea modificar otro dato? Si/no\n")
    if consultar == "Si":
        return True
    else:
        return False

