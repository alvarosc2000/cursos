def sumaMaxima(cadena):
    max_suma = cadena[0]
    suma = 0
    for i in range(len(cadena)):
        suma += cadena[i]

        if suma > max_suma:
            max_suma = suma
        
        if suma < 0:
            suma = 0
    
    return max_suma

# Pruebas
print(sumaMaxima([3, -2, 5, -1]))          # 6
print(sumaMaxima([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
print(sumaMaxima([-1, -2, -3, -4]))        # -1