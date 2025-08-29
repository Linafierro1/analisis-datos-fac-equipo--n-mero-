# analisis_familiar.py
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos
df = df = pd.read_excel(r"C:\Users\jpedrazag\Downloads\JEFAB_2024.xlsx")

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

import matplotlib.pyplot as plt

df['MALTRATO_INTRAFAMILIAR'].value_counts().plot(kind='bar')
plt.title("Casos de Maltrato Intrafamiliar")
plt.xlabel("Maltrato Intrafamiliar")
plt.ylabel("Número de personas")
plt.show()
