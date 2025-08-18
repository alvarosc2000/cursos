def transpuesta(matriz):
    transpuestamatriz = []
    for j in range(len(matriz[0])):  # columnas
        nueva_fila = []
        for i in range(len(matriz)):  # filas
            nueva_fila.append(matriz[i][j])
        transpuestamatriz.append(nueva_fila)

    # imprimir resultado
    for fila in transpuestamatriz:
        print(fila)


hotel = [
    [1, 2, 3],
    [4, 5, 6]
]

transpuesta(hotel)
