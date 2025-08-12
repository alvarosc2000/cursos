cadena = "abc12345"

def validar_contraseña(cadena):
    contador_dig = 0
    contador_letra_may = 0
    contador_letra_min = 0
    contador_espacios = 0

    if len(cadena) < 8:
        return False
    else:
        for i in range(len(cadena)):
            if (cadena[i] == " "):
                contador_espacios +=1
            elif (cadena[i].isupper()):
                contador_letra_may +=1
            elif (cadena[i].islower()):
                contador_letra_min +=1
            elif (cadena[i].isnumeric()):
                contador_dig += 1

    if (contador_espacios >= 1 or contador_letra_may == 0 or contador_letra_min == 0 or contador_dig == 0):
        return False
    else:
        return True

print(validar_contraseña(cadena))