def prodMaxAdy(cadena):
    producto = 0
    for i in range(len(cadena)-1):
        if cadena[i] * cadena[i+1] > producto:
            producto = cadena[i] * cadena[i+1]
    
    return producto


print(prodMaxAdy([3, 6, -2, -5, 7, 3]))