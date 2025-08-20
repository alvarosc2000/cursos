def chessBoardCellColor(cell1, cell2):
    # Convertimos la letra a número: 'A'->1, 'B'->2, ..., 'H'->8
    col1 = ord(cell1[0].upper()) - ord('A') + 1
    col2 = ord(cell2[0].upper()) - ord('A') + 1

    # Convertimos la fila a número
    row1 = int(cell1[1])
    row2 = int(cell2[1])

    # Una celda es negra si la suma de columna + fila es par, blanca si es impar
    color1 = (col1 + row1) % 2
    color2 = (col2 + row2) % 2

    # Si ambos colores coinciden, son del mismo color
    return color1 == color2

# Pruebas
print(chessBoardCellColor("A1", "C3"))  # True
print(chessBoardCellColor("A1", "H3"))  # False
print(chessBoardCellColor("B2", "G7"))  # True
print(chessBoardCellColor("D5", "F2"))  # False
