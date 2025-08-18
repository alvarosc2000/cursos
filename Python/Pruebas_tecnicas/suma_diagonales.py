def sumaDiagonales(matriz):
    sumaD1 = 0
    sumaD2 = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:  # diagonal principal
                sumaD1 += matriz[i][j]
            if i + j == len(matriz) - 1:  # diagonal secundaria
                sumaD2 += matriz[i][j]
    
    return sumaD1, sumaD2


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

d1, d2 = sumaDiagonales(matriz)
print(f"Diagonal principal: {d1}")
print(f"Diagonal secundaria: {d2}")
