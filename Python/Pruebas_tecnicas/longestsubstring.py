def longestsubstring(cadena):
    max_long = 1  # Mínimo tamaño de cualquier substring es 1
    actual = 1    # Contador de la longitud actual
    
    for i in range(len(cadena)-1):
        if cadena[i] <= cadena[i+1]:
            actual += 1
        else:
            if actual > max_long:
                max_long = actual
            actual = 1  # Reiniciamos contador
    
    # Revisamos al final en caso de que la última secuencia sea la más larga
    if actual > max_long:
        max_long = actual
    
    return max_long

# Pruebas
print(longestsubstring("abcabcd"))   # 4 -> "abcd"
print(longestsubstring("abac"))      # 2 -> "ab"
print(longestsubstring("zyx"))       # 1
