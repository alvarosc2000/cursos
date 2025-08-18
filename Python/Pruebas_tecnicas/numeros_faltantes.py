def makeArrayConsecutive2(cadena):
    cadena = sorted(cadena)
    contador = 0
    faltantes = []

    for i in range(len(cadena)-1):
        diferencia = cadena[i+1] - cadena[i]
        if diferencia > 1:
            contador += diferencia - 1
            # Agregar los números que faltan
            for n in range(cadena[i]+1, cadena[i+1]):
                faltantes.append(n)

    return contador, faltantes

contador, faltantes = makeArrayConsecutive2([6, 2, 3, 8])

print(f"Contador --> {contador}")
print(f"Faltantes --> {faltantes}")
