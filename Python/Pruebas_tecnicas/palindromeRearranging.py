def palindromeRearranging(palindromo):
    long = len(palindromo)
    revisadas = []  # lista de letras que ya contamos

    if long % 2 == 0:
        for ch in palindromo:
            if ch not in revisadas:
                if palindromo.count(ch) % 2 != 0:
                    return False
                revisadas.append(ch)
        return True
    else:
        contador = 0
        for ch in palindromo:
            if ch not in revisadas:
                if palindromo.count(ch) % 2 != 0:
                    contador += 1
                revisadas.append(ch)
        return contador == 1

# Pruebas
print(palindromeRearranging("aabbc"))  # True
print(palindromeRearranging("abc"))    # False
print(palindromeRearranging("aabb"))   # True
print(palindromeRearranging("aaa"))    # True
