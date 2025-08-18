def adjacentElmentsProduct(inputArray):
    producto_mas_largo = 0
    pareja = []

    for i in range(len(inputArray)-1):
        if producto_mas_largo < (inputArray[i]*inputArray[i+1]):
            producto_mas_largo = inputArray[i]*inputArray[i+1]
            pareja = [i,i+1]
    
    return producto_mas_largo, pareja

l,p = adjacentElmentsProduct([3,-6,-2,-5,7,3])

print(f"El producto mas largo da como resultado {l}")
print(f"La pareja es {p}")