# demografia_basica.py
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Leer los datos
df = pd.read_excel('datos/JEFAB_2024_v2.xlsx')

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

# 👉 Agrega 'Sin dato' y rellena NA sin romper categorías
df[COL_RANGO] = df[COL_RANGO].cat.add_categories(["Sin dato"]).fillna("Sin dato")


# Estandarizar EDAD_RANGO
df[COL_RANGO] = df[COL_RANGO].astype('string').str.strip()
df[COL_RANGO] = df[COL_RANGO].replace({'nan': pd.NA})  # si viene como texto 'nan'

df[COL_RANGO] = pd.Categorical(
    df[COL_RANGO],
    categories=RANGOS_ORDENADOS,
    ordered=True
)

# Estandarizar SEXO (si viene con minúsculas o espacios)
df[COL_SEXO] = df[COL_SEXO].astype('string').str.strip().str.upper()

print('Valores únicos SEXO:', df[COL_SEXO].dropna().unique())
print('Valores únicos EDAD_RANGO (sin NA):', pd.Series(df[COL_RANGO]).dropna().unique())
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
display(freq_general.head(12))

# Por sexo
freq_hombres = tabla_frecuencias(df.loc[df[COL_SEXO]=='HOMBRE', COL_RANGO], incluir_na=True)
freq_mujeres = tabla_frecuencias(df.loc[df[COL_SEXO]=='MUJER', COL_RANGO], incluir_na=True)

print('\n— HOMBRES —')
display(freq_hombres.head(12))

print('\n— MUJERES —')
display(freq_mujeres.head(12))

# Modas (excluyendo NA)
mg_val, mg_pct = moda_rango(df[COL_RANGO])
mh_val, mh_pct = moda_rango(df.loc[df[COL_SEXO]=='HOMBRE', COL_RANGO])
mm_val, mm_pct = moda_rango(df.loc[df[COL_SEXO]=='MUJER', COL_RANGO])

print('\n=== MODAS DE EDAD_RANGO (Excluyendo NA) ===')
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