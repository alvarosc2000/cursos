def prodMax(lista):
    producto = 0
    valores = []

    for i in range(len(lista)-1):
        if lista[i] * lista[i+1] > producto:
            producto = lista[i] * lista[i+1]
            valores = [lista[i],lista[i+1]]
        
    return producto, valores

productos, valores = prodMax([3, 6, -2, -5, 7, 3])
print(f"El producto es {productos}")
print(f"Los valores son: {valores}")