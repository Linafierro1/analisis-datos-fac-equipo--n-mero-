# calidad_datos.py

import pandas as pd
import missingno as msno

# Leer los datos
df = pd.read_excel('datos/JEFAB_2024.xlsx')

# Cambio de variables

for i in range(len(df)):
    if df.loc[i, "HIJOS"] == "NO":
        df.loc[i, "NUMERO_HIJOS"] = 0
        df.loc[i, "HIJOS_EN_HOGAR"] = 0

# Convertir variables categóricas

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("category")

#Exportar resultado

df.to_excel("datos/JEFAB_2024_v2.xlsx", index=False)

# Análisis de datos faltantes

print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
print("Top 10 columnas con más datos faltantes:")
missing_info = pd.DataFrame({
    'Columna': missing_data.index,
    'Datos_Faltantes': missing_data.values,
    'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)
print(missing_info.head(10))

# Cantidad de datos presentes por variable
col = missing_info["Columna"].head(10)
miss = df[col]
msno.bar(miss, sort= "descending", color = "lightcoral")

# Mapa de calor de faltantes

msno.heatmap(df)

# Análisis de duplicados
print(f"\n=== ANÁLISIS DE DUPLICADOS ===")
print(f"Registros duplicados: {df.duplicated().sum()}")

# Análisis de tipos de datos
print(f"\n=== TIPOS DE DATOS ===")
print(df.dtypes.value_counts().head(6))

# Identificar columnas problemáticas
print(f"\n=== COLUMNAS CON CARACTERES ESPECIALES ===")
problematic_columns = [col for col in df.columns if 'Ã' in col or 'â' in col]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns[:5]:
    print(f"  - {col}")