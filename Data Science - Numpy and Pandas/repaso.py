# repaso_python_ejercicios.py
# Repaso interactivo de Python: listas, funciones, diccionarios, bucles y comprensión de listas

print("=== REPASO DE PYTHON CON EJEMPLOS Y EJERCICIOS ===\n")

# -------------------------
# 1. Creación de listas
# -------------------------
print("1. Creación de listas")
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
print("Lista de números:", numeros)
print("Lista de frutas:", frutas)

# Ejercicio: crea una lista de tus colores favoritos
colores = ["rojo", "azul", "verde"]  # <- Modifica aquí con tus colores
print("Tus colores favoritos:", colores, "\n")

# -------------------------
# 2. Extracción y modificación de datos
# -------------------------
print("2. Extracción y modificación de datos")
print("Primer fruta:", frutas[0])
frutas[1] = "pera"
frutas.append("naranja")
print("Frutas modificadas:", frutas)

# Ejercicio: elimina la última fruta y agrega "kiwi"
frutas.pop()  # eliminar última fruta
frutas.append("kiwi")  # agregar nueva fruta
print("Frutas después del ejercicio:", frutas, "\n")

# -------------------------
# 3. Funciones built-in
# -------------------------
print("3. Funciones built-in")
print("Máximo de numeros:", max(numeros))
print("Suma de numeros:", sum(numeros))

# Ejercicio: calcula el mínimo de la lista numeros
minimo = min(numeros)
print("Mínimo de numeros:", minimo, "\n")

# -------------------------
# 4. Creación de funciones y argumentos flexibles
# -------------------------
print("4. Funciones y argumentos flexibles")
def saludar(nombre):
    return f"Hola, {nombre}!"

def suma(*args):
    return sum(args)

print(saludar("Ana"))
print("Suma 1+2+3:", suma(1, 2, 3))

# Ejercicio: crea una función que reciba un nombre y edad y devuelva un mensaje
def info_persona(nombre, edad):
    return f"{nombre} tiene {edad} años."

print(info_persona("Luis", 25), "\n")

# -------------------------
# 5. Funciones lambda
# -------------------------
print("5. Funciones lambda")
doble = lambda x: x*2
print("Doble de 5:", doble(5))

# Ejercicio: crea una lambda que eleve un número al cuadrado
cuadrado = lambda x: x**2
print("Cuadrado de 4:", cuadrado(4), "\n")

# -------------------------
# 6. Diccionarios
# -------------------------
print("6. Diccionarios")
persona = {"nombre": "Ana", "edad": 25}
print("Persona:", persona)
persona["profesion"] = "Ingeniera"
print("Persona actualizada:", persona)

# Ejercicio: crea un diccionario con tus datos (nombre, edad, ciudad)
mis_datos = {"nombre": "Maria", "edad": 28, "ciudad": "Madrid"}
print("Mis datos:", mis_datos, "\n")

# -------------------------
# 7. Uso de zip
# -------------------------
print("7. Uso de zip")
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 20]
combinado = list(zip(nombres, edades))
print("Combinado:", combinado)

# Ejercicio: usando zip, crea un diccionario nombre:edad
dicc_mayores = {nombre: edad for nombre, edad in zip(nombres, edades) if edad > 21}
print("Diccionario mayores de 21:", dicc_mayores, "\n")

# -------------------------
# 8. Bucles
# -------------------------
print("8. Bucles")
print("Bucle for sobre numeros:")
for n in numeros:
    print(n, end=" ")
print()

# Ejercicio: imprime solo los números pares de la lista
print("Números pares de la lista:")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
print("\n")

# -------------------------
# 9. Comprensión de listas
# -------------------------
print("9. Comprensión de listas")
cuadrados = [x**2 for x in range(6)]
print("Cuadrados:", cuadrados)

# Ejercicio: crea una lista con los números impares entre 0 y 10
impares = [x for x in range(11) if x % 2 != 0]
print("Números impares entre 0 y 10:", impares, "\n")

# -------------------------
# 10. Ejercicio final de integración
# -------------------------
print("10. Ejercicio final: crear diccionario de mayores de edad")
nombres = ["Ana", "Luis", "Pedro", "Maria"]
edades = [20, 25, 19, 30]

# Crea un diccionario nombre:edad solo si la edad es mayor de 21
mayores = {nombre: edad for nombre, edad in zip(nombres, edades) if edad > 21}
print("Mayores de 21 años:", mayores)

print("\n=== FIN DEL REPASO ===")
