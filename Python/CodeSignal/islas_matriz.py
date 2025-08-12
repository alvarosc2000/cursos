def contar_islas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    
    visitado = [[False]*columnas for _ in range(filas)]
    
    def dfs(i, j):
        # Verificar límites y si ya fue visitado o es agua
        if i < 0 or i >= filas or j < 0 or j >= columnas:
            return
        if matriz[i][j] == 0 or visitado[i][j]:
            return
        
        visitado[i][j] = True
        
        # Explorar vecinos: arriba, abajo, izquierda, derecha
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    
    contador_islas = 0
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 1 and not visitado[i][j]:
                dfs(i, j)
                contador_islas += 1
    
    return contador_islas

# Prueba
matriz_ejemplo = [
    [1,1,0,0,0],
    [1,0,0,1,1],
    [0,0,0,1,1]
]

print(contar_islas(matriz_ejemplo))  # Salida: 2
