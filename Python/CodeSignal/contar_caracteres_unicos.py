def count_unique_chars(s):
    s = s.lower()            # Convertir todo a minúsculas
    s = s.replace(" ", "")   # Eliminar espacios
    new_array = []
    for char in s:
        if char not in new_array:
            new_array.append(char)
    return len(new_array)

# Ejemplo para probar
print(count_unique_chars("Hello World"))  # Output esperado: 7
print(count_unique_chars("aaa bbb ccc"))  # Output esperado: 3
