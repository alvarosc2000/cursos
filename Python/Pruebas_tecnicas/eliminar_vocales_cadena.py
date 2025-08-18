def eliminarvocales(cadena):
    aux = ""
    vocales = {'a','e','i','o','u'}

    for i in range(len(cadena)):
        if cadena[i].lower() not in vocales:  # comparo en minúsculas
            aux += cadena[i]                  # conservo la forma original
    
    return aux

print(eliminarvocales("Arbol"))   # Output: "rbl"
print(eliminarvocales("Hola Mundo"))  # Output: "Hl Mnd"
