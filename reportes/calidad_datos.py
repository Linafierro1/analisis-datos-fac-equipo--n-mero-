# calidad_datos.py

import pandas as pd
import missingno as msno 
import matplotlib.pyplot as plt

# Leer los datos
df = pd.read_excel('datos\\JEFAB_2024.xlsx')


# Cambio de variables

for i in range(len(df)):
    if df.loc[i, "HIJOS"] == "NO":
        df.loc[i, "NUMERO_HIJOS"] = 0
        df.loc[i, "HIJOS_EN_HOGAR"] = 0

# Convertir variables categóricas

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("category")


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
plt.show()

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

# selección de variables relevantes
cols = ["ESTADO_CIVIL", "RELACION_PAREJA_ESTABLE", "TIPOLOGIA_FAMILIAR", "HIJOS", "NUMERO_HIJOS", "HIJOS_EN_HOGAR", "MIEMBROS_COMPARTE_VIVIENDA", "VIVIENDA_PROPIA", 
        "VIVE_EN_ARRIENDO", "PERSONA_APOYO_PROBLEMAS", "INTEGRANTE_RED_APOYO", "ACTIVIDADES_FAMILIARES_TIMPO_LIBRE", "MALTRATO_INTRAFAMILIAR", "DISCAPACIDAD","SEXO", 
        "GENERO", "EDAD2", "EDAD_RANGO", "GRADO", "CATEGORIA", "ESTRATO", "NIVEL_EDUCATIVO"]

for col in df.columns:
    if col not in cols:
        df.drop(col, axis=1, inplace=True)

df.dropna(inplace=True)

#Exportar resultado

df.to_excel("datos/JEFAB_2024_v2.xlsx", index=False)