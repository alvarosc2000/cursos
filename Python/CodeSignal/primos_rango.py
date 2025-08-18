def primes_up_to_n(n):
    primos = []
    for num in range(2, n + 1):
        contador = 0
        for i in range(1, num + 1):
            if num % i == 0:
                contador += 1
        if contador == 2:
            primos.append(num)
    return primos

# Ejemplos:
print(primes_up_to_n(10))  # [2, 3, 5, 7]
print(primes_up_to_n(2))   # [2]
print(primes_up_to_n(1))   # []
