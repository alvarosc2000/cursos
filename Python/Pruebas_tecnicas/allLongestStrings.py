def allLongestStrings(inputArray):
    # Paso 1: Encontrar la longitud máxima
    max_len = 0
    for s in inputArray:
        if len(s) > max_len:
            max_len = len(s)

    # Paso 2: Crear una lista vacía para los resultados
    result = []

    # Paso 3: Recorrer la lista y agregar solo los strings con longitud máxima
    for s in inputArray:
        if len(s) == max_len:
            result.append(s)

    return result

# Prueba
print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))  # ["aba", "vcd", "aba"]
