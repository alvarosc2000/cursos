def es_identificador_valido(s):
    for i in range(len(s)):
        first = s[0]
        if first == "_" or first.isalpha():
            return True
        else:
            return False


# Pruebas rápidas
print(es_identificador_valido("a1_b"))  # True
print(es_identificador_valido("1abc"))  # False
