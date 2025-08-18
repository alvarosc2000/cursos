def matrixElementsSum(matrix):
    # 1. Acumulador del precio total
    total = 0
    
    # 2. Conjunto para guardar columnas bloqueadas (malditas)
    bloqueadas = set()
    
    # 3. Recorrer cada fila de la matriz
    for i in range(len(matrix)):
        
        # 4. Recorrer cada columna dentro de esa fila
        for j in range(len(matrix[i])):
            
            # 5. Verificar si la columna ya está maldita
            if j in bloqueadas:
                continue  # saltamos esta habitación
            
            # 6. Si la habitación actual es 0 → se bloquea la columna
            if matrix[i][j] == 0:
                bloqueadas.add(j)
            else:
                # 7. Caso válido: sumamos el precio
                total += matrix[i][j]
    
    # 8. Al terminar, devolvemos el total acumulado
    return total
