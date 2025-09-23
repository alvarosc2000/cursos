import pandas as pd
import numpy as np

# =====================================================
# EXAMEN DE PANDAS – PRACTICA
# =====================================================

# -----------------------------
# 1. CREAR DATAFRAME DESDE DICCIONARIO
# -----------------------------
info_estudiantes = {
    "Nombre": ["Ana", "Luis", "Pedro", "Marta", "Lucia"],
    "Nota_Matematicas": [8, 7, 5, 9, 6],
    "Nota_Lengua": [7, 8, 6, 9, 7],
    "Curso": ["A", "A", "B", "B", "A"]
}

df = pd.DataFrame(info_estudiantes)
print("DataFrame original:")
print(df)
print("\n-----------------\n")

# =====================================================
# 2. SELECCIÓN Y FILTRADO
# =====================================================
print("Columna 'nombre': ")
print(df['Nombre'])
print("\n-----------------\n")

print("Columna cuya nota de matematicas seria >= 7")
print(df[df["Nota_Matematicas"] >= 7])
print("\n-----------------\n")

print("Primera fila")
print(df.iloc[0])
print("\n-----------------\n")

print("Columna nombre que contiene la letra a")
filtro_nombre = df[df["Nombre"].str.contains("a", case=False)]
print(filtro_nombre)
print("\n-----------------\n")

# =====================================================
# 3. COLUMNAS CON CONDICIONALES Y LAMBDA
# =====================================================
df["Resultado"] = np.where(df["Nota_Matematicas"] >= 6, "Aprobado", "Reprobado")

df["Promedio"] = (df["Nota_Matematicas"] + df["Nota_Lengua"]) / 2

categorias = {5: "Bajo", 6: "Bajo", 7: "Medio", 8: "Medio", 9: "Alto", 10: "Alto"}
df["Categoria"] = df["Nota_Matematicas"].map(categorias)

df["Mensaje"] = df.apply(lambda x: f"{x['Nombre']} tiene promedio {x['Promedio']}", axis=1)

print("DataFrame con nuevas columnas (Resultado, Promedio, Categoria, Mensaje):")
print(df)
print("\n-----------------\n")

# =====================================================
# 4. ESTADÍSTICAS Y LIMPIEZA
# =====================================================
mediana_mate = df["Nota_Matematicas"].median()
df["Matematica_Acumulada"] = df["Nota_Matematicas"].cumsum()

print(f"Mediana Matemáticas: {mediana_mate}")
print(df[["Nota_Matematicas", "Matematica_Acumulada"]])
print("\n-----------------\n")

# Ejemplo: reemplazo de NaN
df.loc[2, "Nota_Lengua"] = np.nan  # meto un NaN para probar
df["Nota_Lengua"].fillna(df["Nota_Lengua"].median(), inplace=True)

# Eliminar duplicados
df_sin_duplicados = df.drop_duplicates()
df_sin_duplicados_nombre = df.drop_duplicates(subset=["Nombre"])

print("DataFrame sin duplicados:")
print(df_sin_duplicados)
print("\n-----------------\n")

# Interpolación (ejemplo)
df.loc[4, "Nota_Matematicas"] = np.nan
df["Nota_Matematicas"] = df["Nota_Matematicas"].interpolate(method="linear")

print("DataFrame tras interpolación:")
print(df)
print("\n-----------------\n")

# =====================================================
# 5. ORDENAMIENTO Y AGRUPACIÓN
# =====================================================
df_ordenado = df.sort_values(by="Nota_Matematicas", ascending=False)
print("Ordenado por Nota_Matematicas descendente:")
print(df_ordenado)
print("\n-----------------\n")

pivot = df.pivot_table(values=["Nota_Matematicas", "Nota_Lengua"], index="Curso", aggfunc="mean")
print("Pivot Table (promedio por curso):")
print(pivot)
print("\n-----------------\n")

grouped = df.groupby("Curso")[["Nota_Matematicas", "Nota_Lengua"]].mean()
print("GroupBy (promedio por curso):")
print(grouped)
print("\n-----------------\n")

# =====================================================
# 6. CONCATENACIÓN Y MERGE
# =====================================================
df_extra = pd.DataFrame({
    "Nombre": ["Juan", "Sofia"],
    "Nota_Matematicas": [6, 9],
    "Nota_Lengua": [7, 8],
    "Curso": ["B", "A"]
})
df_concat = pd.concat([df, df_extra], ignore_index=True)

df_info = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Pedro", "Marta", "Lucia", "Juan", "Sofia"],
    "Edad": [15, 16, 17, 16, 15, 17, 16],
    "Genero": ["F", "M", "M", "F", "F", "M", "F"]
})
df_final = pd.merge(df_concat, df_info, on="Nombre")

print("DataFrame final tras concatenación y merge:")
print(df_final)
print("\n-----------------\n")

# =====================================================
# 7. TRABAJO CON CADENAS DE TEXTO
# =====================================================
df_final["Primer_Nombre"] = df_final["Nombre"].str.split().str[0]
df_final["Saludo"] = "Hola, " + df_final["Nombre"]

print("DataFrame con columnas de texto (Primer_Nombre, Saludo):")
print(df_final)
print("\n-----------------\n")

# =====================================================
# 8. IMPRIMIR DATAFRAME FINAL
# =====================================================
print("DataFrame final tras todos los ejercicios:")
print(df_final)
