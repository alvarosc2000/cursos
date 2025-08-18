def is_prime(n):
    if n < 2:
        return False
    contador = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    return contador == 2

# Ejemplos:
print(is_prime(2))   # True
print(is_prime(4))   # False
print(is_prime(17))  # True
print(is_prime(1))   # False
