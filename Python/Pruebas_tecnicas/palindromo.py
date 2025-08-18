def palindromo(cadena):
    for i in range(0, len(cadena)//2):
        if cadena[i] != cadena[-(i+1)]:
            return False
    return True

print(palindromo("oso"))