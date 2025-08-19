def rotateImage(a):
    # Transponer la matriz
    for i in range(len(a)):
        for j in range(i, len(a)):
            a[i][j], a[j][i] = a[j][i], a[i][j]  # intercambiar elementos

    # Invertir cada fila
    for row in a:
        row.reverse()

    return a

# Pruebas
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(rotateImage(matrix))  
# [[7,4,1],[8,5,2],[9,6,3]]
