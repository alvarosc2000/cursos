def invertir_cadena(cadena):
    cadena_aux = ""
    for i in range(len(cadena)-1,-1,-1):
        cadena_aux += cadena[i]

    return cadena_aux


print(invertir_cadena("hola mundo"))