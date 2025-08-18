def contador(cadena):
    cadena = cadena.lower()
    contador_caracteres = 0
    contador_numeros = 0
    contador_letras = 0

    for i in range(len(cadena)):
        if cadena[i].isalpha():
            contador_letras+=1
        elif cadena[i].isdigit():
            contador_numeros+=1
        else:
            contador_caracteres+=1
    
    return contador_caracteres, contador_numeros, contador_letras


c,n,l = (contador("Hola 123 ... adsd32"))
print(f"Los caracteres son: {c}")
print(f"Las letras son: {l}")
print(f"Los numeros son: {n}")