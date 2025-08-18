def islucky(numero):
    numero = str(numero)
    suma1 = 0
    suma2 = 0
    for i in range(len(numero)//2):
        suma1 += int(numero[i])

    for j in range(len(numero)//2, len(numero)):
        suma2+= int(numero[j])

    if suma1 == suma2:
        return True
    else:
        return False


print(islucky(1230))