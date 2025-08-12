def fibonacci_modificado(nums):
    cadena = []
    for i in range(len(nums)):
        if i < 2:
            cadena.append(nums[i])
        else:
            cadena.append(cadena[i-1] + cadena[i-2])
    return cadena
    

# Ejemplo para probar
print(fibonacci_modificado([1, 1, 0, 0, 0, 0]))  # Salida esperada: [1, 1, 2, 3, 5, 8]
