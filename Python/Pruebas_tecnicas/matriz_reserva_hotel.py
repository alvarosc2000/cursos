def is_available(matrix, row, col):
    return matrix[row][col] == 0  # True si está libre, False si está ocupado

def book_room(matrix, row, col):
    if matrix[row][col] == 0:
        matrix[row][col] = 1
        # Mostrar toda la matriz
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()  # salto de línea por fila
    else:
        print("Not available")

def cancel_booking(matrix, row, col):
    if matrix[row][col] == 0:
        print("Ya estaba vacia")
    else:
        matrix[row][col] = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


hotel = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

print(is_available(hotel, 0, 2))  # True
print(is_available(hotel, 0, 0))  # False
book_room(hotel, 1, 0)
cancel_booking(hotel,1,0)