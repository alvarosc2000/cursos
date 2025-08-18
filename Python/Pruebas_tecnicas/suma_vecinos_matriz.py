def sumavecinos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Inicializar vecinos en 0
            vecino_arriba = matriz[i-1][j] if i-1 >= 0 else 0
            vecino_abajo = matriz[i+1][j] if i+1 < len(matriz) else 0
            vecino_izquierda = matriz[i][j-1] if j-1 >= 0 else 0
            vecino_derecha = matriz[i][j+1] if j+1 < len(matriz[i]) else 0

            # Sumarlos
            matriz[i][j] = vecino_arriba + vecino_abajo + vecino_izquierda + vecino_derecha

    return matriz

# Ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sumavecinos(matriz))
