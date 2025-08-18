def eliminarVocales(cadena):
    cadena_new = ""
    conjunto = {'a','e','i','o','u'}

    for i in range(len(cadena)):
        if cadena[i] not in conjunto:
            cadena_new += cadena[i]
    
    return cadena_new


print(eliminarVocales("solo"))