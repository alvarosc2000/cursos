def es_identificador_valido(cadena):
    first = cadena[0]
    if first == "_" or first.isalpha():
        return True
    else:
        return False


# Pruebas rápidas
print(es_identificador_valido("a1_b"))  # True
print(es_identificador_valido("1abc"))  # False