def suma_digitos(numero):
    numero = str(numero)
    suma = 0
    for i in range(len(numero)):
        suma += int(numero[i])
    return suma

print(suma_digitos(29))