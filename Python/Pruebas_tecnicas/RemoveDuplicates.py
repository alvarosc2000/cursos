def eliminar_duplicados(cadena):
    cadena2 = ""
    for i in range(len(cadena)):
        if cadena[i] not in cadena2:
            cadena2 += (cadena[i])
    
    return cadena2

print(eliminar_duplicados("Hola mundo"))