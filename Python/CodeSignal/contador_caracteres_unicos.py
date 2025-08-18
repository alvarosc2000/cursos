def count_unique_chars(s):
    contador = 0
    cadena = ""
    for i in range(len(s)):
        if s[i] not in cadena and s[i] != " ":
            cadena = cadena + s[i]
            contador += 1
    return contador

# Ejemplos:
print(count_unique_chars("Hello World"))  # 7
print(count_unique_chars("aaa bbb ccc"))  # 3
