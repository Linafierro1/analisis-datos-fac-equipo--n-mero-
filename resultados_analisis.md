# Resultados relevantes
---

## Análisis de Calidad de Datos
El análisis de la base **JEFAB_2024.xlsx** (6.423 registros y 231 variables) mostró que la estructura de los datos es consistente, sin duplicados, pero con **19.831 valores faltantes** concentrados en variables clave como número de hijos, personas en el hogar y edades de padres; el script `calidad_datos.py` corrige automáticamente valores relacionados con hijos, convierte variables categóricas para optimizar el análisis y genera una nueva versión de la base limpia, aunque persisten problemas de **codificación de caracteres** que afectan algunas variables de texto; en conclusión, la base es sólida para análisis, pero requiere imputación de faltantes o selección de variables con poca presencia de faltantes y corrección de encoding antes de avanzar a etapas analíticas más complejas.


---
## Análisis Demográfico

La población analizada de la FAC está conformada mayoritariamente por **hombres (≈69%)** frente a un **31% de mujeres**, con una **edad promedio de 36,7 años** y un rango etario predominante entre **33–37 años** en ambos géneros. Aunque la moda es compartida, la distribución revela diferencias: los hombres se concentran más en tramos jóvenes e intermedios (18–37 años), mientras que las mujeres presentan mayor peso relativo en edades medias y avanzadas (43–52 y algunos casos mayores de 58 años). En cuanto al **grado militar**, al excluir la categoría “No responde”, en hombres predominan los **suboficiales técnicos (T1, T2, T3)**, mientras que en mujeres se observa una participación más equilibrada, con presencia destacada de **oficiales en grados iniciales (CT, TE, ST)**. Esto refleja contrastes tanto en la estructura etaria como en la composición jerárquica por género.
