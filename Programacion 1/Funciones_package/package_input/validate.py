validacion_numero = while numero < minimo or numero > maximo:
    numero = input(f"Maaaaaaal!! {mensaje_error}")
    numero = int(numero)
    vueltas += 1
    if vueltas == reintentos - 1:
    return None