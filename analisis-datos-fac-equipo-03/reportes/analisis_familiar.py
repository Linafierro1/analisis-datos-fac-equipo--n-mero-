# analisis_familiar.py
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos
df = pd.read_excel('datos/JEFAB_2024.xlsx')

# An�lisis de estado civil
print("=== AN�LISIS ESTADO CIVIL ===")
print(df['ESTADO_CIVIL'].value_counts())

# An�lisis de hijos
print("\n=== AN�LISIS DE HIJOS ===")
print(f"Personal con hijos: {df['HIJOS'].value_counts()}")

# An�lisis de convivencia familiar
print("\n=== AN�LISIS DE CONVIVENCIA ===")
print(f"Habita con familia: {df['HABITA_VIVIENDA_FAMILIAR'].value_counts()}")

# Gr�fico de estado civil
plt.figure(figsize=(10, 6))
df['ESTADO_CIVIL'].value_counts().plot(kind='bar')
plt.title('Distribuci�n del Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
