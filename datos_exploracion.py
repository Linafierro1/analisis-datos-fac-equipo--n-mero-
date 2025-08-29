# datos_exploracion.py (archivo principal conjunto)
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

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
plt.show()

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

# Limpiar filas con datos faltantes en columnas clave
df.dropna(inplace=True)

# Explorar estructura básica
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")

# Análisis de edad
print("\n=== ANÁLISIS DE EDAD ===")
print(f"Edad promedio: {df['EDAD2'].mean():.1f} años")
print(f"Edad mínima: {df['EDAD2'].min()} años")
print(f"Edad máxima: {df['EDAD2'].max()} años")
print(f"Edad más frecuente (moda): {df['EDAD2'].mode()[0]} años")

# Columnas esperadas
COL_SEXO = "SEXO"
COL_RANGO = "EDAD_RANGO"
RANGOS_ORDENADOS = [
    "18-22","23-27","28-32","33-37","38-42",
    "43-47","48-52","53-57","58-62","63-67","68-72"
]

# Asegura strings limpios
df[COL_SEXO]  = df[COL_SEXO].astype("string").str.strip().str.upper()

# Categórica ordenada
df[COL_RANGO] = pd.Categorical(df[COL_RANGO], categories=RANGOS_ORDENADOS, ordered=True)


# Estandarizar EDAD_RANGO
df[COL_RANGO] = df[COL_RANGO].astype('string').str.strip()

df[COL_RANGO] = pd.Categorical(
    df[COL_RANGO],
    categories=RANGOS_ORDENADOS,
    ordered=True
)

# Estandarizar SEXO (si viene con minúsculas o espacios)
df[COL_SEXO] = df[COL_SEXO].astype('string').str.strip().str.upper()

print('Valores únicos SEXO:', df[COL_SEXO].unique())
print('Valores únicos EDAD_RANGO (sin NA):', pd.Series(df[COL_RANGO]).unique())
print('Faltantes EDAD_RANGO (%):', round(df[COL_RANGO].isna().mean()*100, 1))

#Funciones auxiliares
def tabla_frecuencias(series, incluir_na=True):
    """Tabla de conteo y porcentaje. Si incluir_na=True, agrega 'Sin dato'."""
    s = series.copy()
    if incluir_na:
        s = s.astype('object').where(~s.isna(), 'Sin dato')
    c = (s.value_counts(dropna=False)
           .rename_axis(series.name)
           .reset_index(name='conteo'))
    total = c['conteo'].sum()
    c['porcentaje'] = (c['conteo'] / total * 100).round(1)
    return c

def moda_rango(series):
    """Devuelve (valor_modal, porcentaje) excluyendo NA ('Sin dato' no compite)."""
    s = series.dropna()
    if s.empty:
        return None, 0.0
    vc = s.value_counts()
    top_val = vc.index[0]
    top_pct = round(vc.iloc[0] / vc.sum() * 100, 1)
    return top_val, top_pct

def top_por_categoria(df, cat_col, rango_col):
    """Top 1 de EDAD_RANGO por cada categoría (p. ej., GRADO o ESTADO_CIVIL)."""
    if cat_col not in df.columns:
        return pd.DataFrame()
    g = df.groupby([cat_col, rango_col], dropna=False).size().reset_index(name='n')
    g['%'] = g.groupby(cat_col)['n'].transform(lambda x: (x / x.sum() * 100).round(1))
    top = (g.sort_values([cat_col, 'n'], ascending=[True, False])
             .groupby(cat_col, as_index=False)
             .head(1))
    return top.sort_values(cat_col)

# General
freq_general = tabla_frecuencias(df[COL_RANGO], incluir_na=True)
print(freq_general.head(12))

# Por sexo
freq_hombres = tabla_frecuencias(df.loc[df[COL_SEXO]=='HOMBRE', COL_RANGO], incluir_na=True)
freq_mujeres = tabla_frecuencias(df.loc[df[COL_SEXO]=='MUJER', COL_RANGO], incluir_na=True)

print('\n— HOMBRES —')
print(freq_hombres.head(12))

print('\n— MUJERES —')
print(freq_mujeres.head(12))

# Modas (excluyendo NA)
mg_val, mg_pct = moda_rango(df[COL_RANGO])
mh_val, mh_pct = moda_rango(df.loc[df[COL_SEXO]=='HOMBRE', COL_RANGO])
mm_val, mm_pct = moda_rango(df.loc[df[COL_SEXO]=='MUJER', COL_RANGO])

print('\n=== MODAS DE EDAD_RANGO ===')
print(f'General : {mg_val} ({mg_pct}%)')
print(f'Hombres : {mh_val} ({mh_pct}%)')
print(f'Mujeres : {mm_val} ({mm_pct}%)')

# Barras – Frecuencia general
plt.figure(figsize=(8,4))
# Reordenar según categoría (ya está en Categorical)
fg_plot = freq_general[freq_general[COL_RANGO] != 'Sin dato'].copy()
fg_plot = fg_plot.set_index(COL_RANGO).reindex(RANGOS_ORDENADOS).reset_index()
plt.bar(fg_plot[COL_RANGO], fg_plot['conteo'])
plt.title('Frecuencia de EDAD_RANGO (General)')
plt.xlabel('EDAD_RANGO')
plt.ylabel('Conteo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Barras – Hombres
plt.figure(figsize=(8,4))
fh_plot = freq_hombres[freq_hombres[COL_RANGO] != 'Sin dato'].copy()
fh_plot = fh_plot.set_index(COL_RANGO).reindex(RANGOS_ORDENADOS).reset_index()
plt.bar(fh_plot[COL_RANGO], fh_plot['conteo'])
plt.title('Frecuencia de EDAD_RANGO (Hombres)')
plt.xlabel('EDAD_RANGO')
plt.ylabel('Conteo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Barras – Mujeres
plt.figure(figsize=(8,4))
fm_plot = freq_mujeres[freq_mujeres[COL_RANGO] != 'Sin dato'].copy()
fm_plot = fm_plot.set_index(COL_RANGO).reindex(RANGOS_ORDENADOS).reset_index()
plt.bar(fm_plot[COL_RANGO], fm_plot['conteo'])
plt.title('Frecuencia de EDAD_RANGO (Mujeres)')
plt.xlabel('EDAD_RANGO')
plt.ylabel('Conteo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Análisis de género
print("\n=== ANÁLISIS DE GÉNERO ===")
print(df['GENERO'].value_counts())

# === 1) Tablas de frecuencias por género ===
freq_hombres = (
    df.loc[df['SEXO'] == 'HOMBRE', 'EDAD_RANGO']
      .value_counts()
      .rename_axis("EDAD_RANGO")
      .reset_index(name="conteo")
      .sort_values("EDAD_RANGO")
)
freq_mujeres = (
    df.loc[df['SEXO'] == 'MUJER', 'EDAD_RANGO']
      .value_counts()
      .rename_axis("EDAD_RANGO")
      .reset_index(name="conteo")
      .sort_values("EDAD_RANGO")
)

# Unir en una sola tabla
tabla_genero = pd.merge(
    freq_hombres, freq_mujeres,
    on="EDAD_RANGO", how="outer", suffixes=("_H", "_M")
)

# Rellenar únicamente las columnas de conteo (numéricas) y dejar EDAD_RANGO intacta
for col in ["conteo_H", "conteo_M"]:
    if col in tabla_genero.columns:
        tabla_genero[col] = tabla_genero[col].fillna(0).astype(int)

# Calcular totales y porcentajes
tabla_genero["total"] = tabla_genero["conteo_H"] + tabla_genero["conteo_M"]
tabla_genero["%_H"]   = (tabla_genero["conteo_H"] / tabla_genero["total"] * 100).round(1)
tabla_genero["%_M"]   = (tabla_genero["conteo_M"] / tabla_genero["total"] * 100).round(1)


print("=== Distribución por rango y sexo ===")
print(tabla_genero)

# === 2) Gráfico comparativo ===
plt.figure(figsize=(10,5))
x = range(len(tabla_genero))
plt.bar([i-0.2 for i in x], tabla_genero["conteo_H"], width=0.4, label="Hombres")
plt.bar([i+0.2 for i in x], tabla_genero["conteo_M"], width=0.4, label="Mujeres")
plt.xticks(x, tabla_genero["EDAD_RANGO"], rotation=45)
plt.title("Distribución de EDAD_RANGO por Género")
plt.xlabel("Rango de edad")
plt.ylabel("Cantidad")
plt.legend()
plt.tight_layout()
plt.show()

# Análisis de grados solo para hombres
print("\n=== ANÁLISIS DE GRADO MILITAR (SOLO HOMBRES) ===")
grados_hombres = df[df['GENERO'] == 'MASCULINO']['GRADO'].value_counts()
print(grados_hombres.head(20))

# Análisis de grados solo para mujeres
print("\n=== ANÁLISIS DE GRADO MILITAR (SOLO MUJERES) ===")
grados_mujeres = df[df['GENERO'] == 'FEMENINO']['GRADO'].value_counts()
print(grados_mujeres.head(15))

# Gráfico de edades
plt.figure(figsize=(10, 6))
plt.hist(df['EDAD2'], bins=20, edgecolor='black')
plt.title('Distribución de Edades del Personal FAC')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Personal')
plt.show()

# === 1. Estado civil ===
print("=== ANÁLISIS ESTADO CIVIL ===")
print(df['ESTADO_CIVIL'].value_counts())

# Porcentaje casados
porc_casados = (df['ESTADO_CIVIL'].eq('CASADO').sum() / len(df)) * 100
print(f"\nPorcentaje de casados: {porc_casados:.2f}%")

# === 2. Hijos ===
print("\n=== ANÁLISIS DE HIJOS ===")
print(df['HIJOS'].value_counts())

# Número de hijos y cuántos conviven con ellos
print("\nNúmero de hijos declarados:")
print(df['NUMERO_HIJOS'].value_counts().head())
print("\nNúmero de hijos en el hogar:")
print(df['HIJOS_EN_HOGAR'].value_counts().head())

# === 3. Relación entre edad y estado civil ===
print("\n=== RELACIÓN EDAD Y ESTADO CIVIL ===")
print(df.groupby('ESTADO_CIVIL')['EDAD2'].mean().round(1))

# === Gráfico estado civil ===
plt.figure(figsize=(8, 5))
df['ESTADO_CIVIL'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribución del Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# === Analisis Familiar ===

print("=== DISTRIBUCIÓN DE MALTRATO INTRAFAMILIAR ===")
print(df['MALTRATO_INTRAFAMILIAR'].value_counts(dropna=False))
print(df['MALTRATO_INTRAFAMILIAR'].value_counts(normalize=True) * 100)

maltrato_estado = pd.crosstab(df['ESTADO_CIVIL'], df['MALTRATO_INTRAFAMILIAR'], normalize='index') * 100
print("=== MALTRATO POR ESTADO CIVIL (%) ===")
print(maltrato_estado)

maltrato_hijos = pd.crosstab(df['HIJOS'], df['MALTRATO_INTRAFAMILIAR'], normalize='index') * 100
print("=== MALTRATO SEGÚN SI TIENE HIJOS (%) ===")
print(maltrato_hijos)

maltrato_num_hijos = pd.crosstab(df['NUMERO_HIJOS'], df['MALTRATO_INTRAFAMILIAR'], normalize='index') * 100
print("=== MALTRATO POR NÚMERO DE HIJOS (%) ===")
print(maltrato_num_hijos)

print("=== EDAD PROMEDIO SEGÚN MALTRATO ===")
print(df.groupby('MALTRATO_INTRAFAMILIAR')['EDAD2'].mean())

df['MALTRATO_INTRAFAMILIAR'].value_counts().plot(kind='bar')
plt.title("Casos de Maltrato Intrafamiliar")
plt.xlabel("Maltrato Intrafamiliar")
plt.ylabel("Número de personas")
plt.show()