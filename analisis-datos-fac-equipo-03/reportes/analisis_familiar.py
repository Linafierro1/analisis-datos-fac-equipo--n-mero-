# analisis_familiar.py
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos
df = pd.read_excel('datos/JEFAB_2024.xlsx')

# Análisis de estado civil
print("=== ANÁLISIS ESTADO CIVIL ===")
print(df['ESTADO_CIVIL'].value_counts())

# Análisis de hijos
print("\n=== ANÁLISIS DE HIJOS ===")
print(f"Personal con hijos: {df['HIJOS'].value_counts()}")

# Análisis de convivencia familiar
print("\n=== ANÁLISIS DE CONVIVENCIA ===")
print(f"Habita con familia: {df['HABITA_VIVIENDA_FAMILIAR'].value_counts()}")

# Gráfico de estado civil
plt.figure(figsize=(10, 6))
df['ESTADO_CIVIL'].value_counts().plot(kind='bar')
plt.title('Distribución del Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
