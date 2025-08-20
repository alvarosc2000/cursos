def avoidObstacles(inputArray):
    max_obstaculo = max(inputArray)  # encontramos el obstáculo más lejano
    salto = 1  # empezamos desde 1

    while True:
        puede_saltar = True
        for obstaculo in inputArray:
            if obstaculo % salto == 0:  # si un obstáculo coincide con el salto
                puede_saltar = False
                break  # no sirve este salto, probamos el siguiente
        if puede_saltar:
            return salto  # encontramos el salto mínimo que evita todos los obstáculos
        salto += 1  # probamos el siguiente salto
        

# Pruebas
print(avoidObstacles([5, 3, 6, 7, 9]))   # 4
print(avoidObstacles([2, 3]))            # 4
print(avoidObstacles([1, 4, 10, 6, 2]))  # 7
