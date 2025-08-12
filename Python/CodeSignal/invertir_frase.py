def invertir_palabras(frase):
    new_frase = ""
    i = len(frase) - 1
    while i >= 0:
        palabra = ""
        while i >= 0 and frase[i] != " ":
            palabra = frase[i] + palabra
            i -= 1
        new_frase += palabra + " "
        i -= 1  # Para saltar el espacio
    return new_frase.strip()

# Ejemplo para probar
print(invertir_palabras("Hola Mundo desde ChatGPT"))  # Salida esperada: "ChatGPT desde Mundo Hola"
