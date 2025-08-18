def palabra_mas_larga(cadena):
    palabra_actual = ""
    palabra_larga = ""
    longitud_maxima = 0

    for caracter in cadena:
        if caracter != " ":
            palabra_actual += caracter
        else:
            if len(palabra_actual) > longitud_maxima:
                palabra_larga = palabra_actual
                longitud_maxima = len(palabra_actual)
            palabra_actual = ""  # reinicio

    # Verificar última palabra (por si no termina en espacio)
    if len(palabra_actual) > longitud_maxima:
        palabra_larga = palabra_actual
        longitud_maxima = len(palabra_actual)

    return palabra_larga


# Ejemplo
print(palabra_mas_larga("el coche es azul"))  # → "coche"
