def ipv4(cadena):
    octeto = ""
    partes = []
    
    # separar en octetos con un bucle
    for i in range(len(cadena)):
        if cadena[i] == ".":   # si encontramos punto, guardamos el octeto
            partes.append(octeto)
            octeto = ""
        else:
            octeto += cadena[i]
    partes.append(octeto)  # último octeto

    # deben ser 4 partes exactas
    if len(partes) != 4:
        return False

    # validar cada parte
    for p in partes:
        if not p.isdigit():   # solo números
            return False
        if len(p) > 1 and p[0] == "0":  # no ceros a la izquierda
            return False
        num = int(p)
        if num < 0 or num > 255:
            return False

    return True


# Pruebas
print(ipv4("172.16.254.1"))     # ✅ True
print(ipv4("256.100.50.25"))    # ❌ False (256 inválido)
print(ipv4("192.168.01.1"))     # ❌ False (01 inválido por cero a la izquierda)
print(ipv4("192.168.1"))        # ❌ False (faltan octetos)
print(ipv4("abc.168.1.1"))      # ❌ False (contiene letras)
