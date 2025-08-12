def suma_vecinos():
    cadena = []
    valor = int(input("Introduce valor (negativo para terminar): "))
    while valor >= 0:
        cadena.append(valor)
        valor = int(input("Introduce valor (negativo para terminar): "))
    
    resultado = []
    for i in range(len(cadena)):
        izquierda = cadena[i - 1] if i - 1 >= 0 else 0
        derecha = cadena[i + 1] if i + 1 < len(cadena) else 0
        resultado.append(izquierda + cadena[i] + derecha)
    
    return resultado

# Ejecución
print(suma_vecinos())
