def contador_vocales_consonantes(palabra):
    palabra = palabra.lower()  # pasamos todo a minúsculas de una vez
    vocales = {'a', 'e', 'i', 'o', 'u'}

    contador_vocales = 0
    contador_consonantes = 0

    for letra in palabra:
        if letra.isalpha():  # solo contamos letras
            if letra in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes


# Ejemplo de uso
v, c = contador_vocales_consonantes("AlvaRo 123 !!!")
print(f"Las vocales son --> {v}")
print(f"Las consonantes son --> {c}")
