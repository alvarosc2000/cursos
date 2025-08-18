def reverse_string(s):
    cadena = ""
    for i in range(len(s)-1,-1,-1):
        cadena = cadena + s[i]
    return cadena

# Ejemplos:
print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
