def rotate_matrix(matrix):
    n = len(matrix)
    
    # Transponer la matriz
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Invertir cada fila
    for row in matrix:
        row.reverse()

# Ejemplo para probar
mat = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate_matrix(mat)
print(mat)  # Output esperado: [[7,4,1],[8,5,2],[9,6,3]]
