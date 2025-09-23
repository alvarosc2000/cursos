import pandas as pd
import numpy as np

# =====================================================
# 1. Crear un DataFrame a partir de un diccionario
# =====================================================
info_pais = {
    "pais": ["Brasil", "Mexico", "España", "Peru", "Colombia", "Venezuela"],
    "capital": ["Brasilia", "Ciudad de mexico", "Madrid", "Lima", "Bogota", "Caracas"],
    "superficie (Mkm2)": [8.5, 1.9, 1.2, 0.5, 1.1, 0.9]
}
df_pais = pd.DataFrame(info_pais)
print("DataFrame completo de países:")
print(df_pais.to_string())
print("\n-----------------\n")

# =====================================================
# 2. Guardar y leer CSV
# =====================================================
df_pais.to_csv("pais.csv", index=False)
df = pd.read_csv("pais.csv")
print("Primeras filas del DataFrame leído desde CSV:")
print(df.head())
print("\nInformación del DataFrame:")
print(df.info())
print("\n-----------------\n")

# =====================================================
# 3. Selección de datos
# =====================================================
print("Columna 'pais':")
print(df['pais'])
print("\nColumnas 'pais' y 'capital':")
print(df[['pais', 'capital']])
print("\nPrimera fila:")
print(df.iloc[0])
print("\nPrimeras tres filas:")
print(df.iloc[0:3])
print("\nPaíses con superficie > 1 Mkm2:")
print(df[df['superficie (Mkm2)'] > 1])
print("\n-----------------\n")

# =====================================================
# 4. DataFrame de estudiantes
# =====================================================
info_estudiantes = {
    "Nombre": ["Javier", "Marta", "Lucia", "Pedro", "Juan", "Maria"],
    "Evaluacion_Matematicas": [5, 7, 8, 4, 10, "NaN"],
    "Evaluacion_Lengua": [8, 9, 7, 5, 8, 6]
}
df_est = pd.DataFrame(info_estudiantes)
print("DataFrame completo de estudiantes:")
print(df_est.to_string())
print("\n-----------------\n")

# =====================================================
# 5. Revisar y reemplazar valores faltantes
# =====================================================
df_est["Evaluacion_Matematicas"] = pd.to_numeric(df_est["Evaluacion_Matematicas"], errors='coerce')
print("Valores faltantes (NaN):")
print(df_est.isna())
mediana_mate = df_est["Evaluacion_Matematicas"].median()
df_est["Evaluacion_Matematicas"].fillna(mediana_mate, inplace=True)
print("\nDataFrame tras reemplazar NaN por mediana:")
print(df_est.to_string())
print("\n-----------------\n")

# =====================================================
# 6. Estadísticas y columna acumulativa
# =====================================================
print("Medianas de evaluaciones:")
print(df_est[["Evaluacion_Matematicas","Evaluacion_Lengua"]].median())
df_est["Matematicas Acumuladas"] = df_est["Evaluacion_Matematicas"].cumsum()
print("\nDataFrame con suma acumulada de Matemáticas:")
print(df_est)
print("\n-----------------\n")

# =====================================================
# 7. Eliminar duplicados
# =====================================================
df_sin_dup = df_est.drop_duplicates()
print("Eliminar duplicados completos:")
print(df_sin_dup)
df_sin_dup = df_est.drop_duplicates(subset=["Nombre"])
print("Eliminar duplicados por 'Nombre':")
print(df_sin_dup)
print("\n-----------------\n")

# =====================================================
# 8. Interpolación de datos
# =====================================================
df_temp = pd.DataFrame({"Dia": [1,2,3,4,5,6], "Temperatura": [20,np.nan,np.nan,26,27,np.nan]})
print("DataFrame original de temperaturas:")
print(df_temp)
df_temp['Temperatura'] = df_temp['Temperatura'].interpolate(method="linear", limit_direction="forward")
print("\nDataFrame tras interpolación lineal:")
print(df_temp)
print("\n-----------------\n")

# =====================================================
# 9. Filtrado de datos
# =====================================================
print("Estudiantes con Matemáticas > 6:")
print(df_est[df_est["Evaluacion_Matematicas"] > 6])
print("\nEstudiantes con Matemáticas > 6 y Lengua > 7:")
print(df_est[(df_est["Evaluacion_Matematicas"] > 6) & (df_est["Evaluacion_Lengua"] > 7)])
print("\nEstudiantes con 'a' en su nombre:")
print(df_est[df_est["Nombre"].str.contains("a")])
print("\n-----------------\n")

# =====================================================
# 10. Ordenar valores
# =====================================================
df_ordenado = df_est.sort_values(by="Evaluacion_Matematicas", ascending=False)
print("Ordenado por Matemáticas descendente:")
print(df_ordenado)
print("\n-----------------\n")

# =====================================================
# 11. Trabajar con cadenas de texto
# =====================================================
df_nombres = pd.DataFrame({"Nombre": ["Javier Pérez","Marta López","Lucia Gómez","Pedro Díaz"]})
df_nombres["Saludo"] = "Hola"
df_nombres["Primer_Nombre"] = df_nombres["Nombre"].str.split().str[0]
print("DataFrame con columnas de texto:")
print(df_nombres)
print("\n-----------------\n")

# =====================================================
# 12. Map y lambda
# =====================================================
categorias = {4:"Bajo",5:"Bajo",6:"Medio",7:"Medio",8:"Alto",10:"Alto"}
df_est["Categoria_Matematicas"] = df_est["Evaluacion_Matematicas"].map(categorias)
df_est["Resultado_Matematicas"] = df_est["Evaluacion_Matematicas"].apply(lambda x: "Aprobado" if x>=6 else "Reprobado")
df_est["Promedio"] = (df_est["Evaluacion_Matematicas"]+df_est["Evaluacion_Lengua"])/2
df_est["Observacion"] = df_est["Promedio"].apply(lambda x: "Excelente" if x>=8 else ("Bueno" if x>=6 else "Regular"))
df_est["Mensaje"] = df_est.apply(lambda row: f"{row['Nombre']} tiene promedio {row['Promedio']}", axis=1)
print("DataFrame final con map y lambda:")
print(df_est)
print("\n-----------------\n")

# =====================================================
# 13. Columnas condicionales, renombrar y reordenar
# =====================================================
df_est["Resultado_Condicional"] = np.where(df_est["Promedio"]>=6,"Aprobado","Reprobado")
df_est.rename(columns={"Evaluacion_Matematicas":"Matematicas","Evaluacion_Lengua":"Lengua"}, inplace=True)
df_est = df_est[["Nombre","Matematicas","Lengua","Promedio","Resultado_Matematicas","Observacion","Mensaje","Resultado_Condicional"]]
print("DataFrame con columnas condicionales y renombradas:")
print(df_est)
print("\n-----------------\n")

# =====================================================
# 14. Pivot table
# =====================================================
df_est["Curso"] = ["A","A","B","B","A","B"]  # Agregar columna para ejemplo
pivot = df_est.pivot_table(index="Curso", values=["Matematicas","Lengua"], aggfunc="mean")
print("Pivot table por Curso:")
print(pivot)
print("\n-----------------\n")

# =====================================================
# 15. Groupby
# =====================================================
grouped = df_est.groupby("Curso")[["Matematicas","Lengua"]].mean()
print("Groupby promedio por Curso:")
print(grouped)
print("\n-----------------\n")

# =====================================================
# 16. Concatenación y combinación
# =====================================================
df_extra = pd.DataFrame({"Nombre":["Carlos","Laura"],"Matematicas":[7,9],"Lengua":[8,10]})
df_concat = pd.concat([df_est,df_extra], ignore_index=True)
print("Concatenación vertical de DataFrames:")
print(df_concat)

df_info = pd.DataFrame({"Nombre":["Javier","Marta","Lucia","Pedro","Juan","Maria","Ana","Carlos","Laura"],
                        "Edad":[15,16,15,16,15,16,15,16,15],
                        "Genero":["M","F","F","M","M","F","F","M","F"]})
df_final = pd.merge(df_concat, df_info, on="Nombre", how="left")
print("\nDataFrame final tras merge con información adicional:")
print(df_final)
