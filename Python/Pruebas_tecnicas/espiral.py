def spiralOrder(matrix):
    res = []
    if not matrix:
        return res

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # recorrer fila superior
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1

        # recorrer columna derecha
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # recorrer fila inferior
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # recorrer columna izquierda
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


# Ejemplo
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# → [1, 2, 3, 6, 9, 8, 7, 4, 5]
