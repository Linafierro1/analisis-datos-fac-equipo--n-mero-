# Informe de Calidad de Datos – JEFAB 2024

## 1. Descripción General
El análisis se realizó sobre la base de datos **JEFAB_2024.xlsx**, que contiene **6.423 registros** y **231 variables**. Se trata de información sociofamiliar y demográfica de una población asociada a unidades de la Fuerza Aeroespacial Colombiana (**FAC**), georeferenciadas con un sistema de coordenadas ubicadas en distintos departamentos de Colombia.

El script `calidad_datos.py` automatizarealiza varias tareas de visualización y diagnóstico, enfocadas en el tratamiento de valores faltantesy presencia en variables categóricas y numéricas, duplicados y detección de problemas de codificación.

---

## 2. Estructura de la Base

Las variables representan características demográficas (edad, sexo, estado civil), composición familiar, condiciones de vivienda, educación militar, y factores socioeconómicos. Con una estructura de:

- **Número de filas:** 6.423  
- **Número de columnas:** 231  
- **Tipos de variables:**  
  - 153 variables numéricas enteras (`int64`).  
  - 12 variables numéricas decimales (`float64`).  
  - 66 variables categóricas/objetos (`object`).  



---

## 3. Procesos de Limpieza Implementados
1. **Corrección de variables de hijos**:  
   Cuando la variable **HIJOS** es `"NO"`, el script ajusta automáticamente `NUMERO_HIJOS = 0` y `HIJOS_EN_HOGAR = 0`.  

2. **Conversión de variables categóricas**:  
   Todas las columnas de tipo `object` se convierten a `category` para optimizar espacio y facilitar análisis.  

3. **Exportación de resultados**:  
   El DataFrame procesado se guarda en un nuevo archivo:  
   `datos/JEFAB_2024_v2.xlsx`.

---

## 4. Análisis de Valores Faltantes
- **Total de valores faltantes:** 19.831.  
- **Variables con más valores faltantes:**  
  1. `NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2` (3928)  61,1%
  2. `NUMERO_HABITAN_VIVIENDA2` (3808)  59,2%
  3. `EDAD_PADRE` (1939)  30,2%
  4. `EDAD_RANGO_PADRE` (1939)  30,2%
  5. `EDAD_RANGO_MADRE` (889)  13,9%
  6. `EDAD_MADRE` (885)  13,8%
  7. `NUMERO_HIJOS` (3217)  7,2%
  8. `HIJOS_EN_HOGAR` (3200)  6,9%
  9. `EDAD2` (13)  0,2%
  10. `EDAD_RANGO` (13)  0,2%
  

Se usaron visualizaciones (`missingno`) para:
- **Distribución de faltantes por variable (barplot).**
- **Mapa de calor de correlación de faltantes:** Generando relaciones consecuentes a la presencia de un dato faltante de una variable a otra, identifica si hay un valor faltante en número de hijos es probable que también habrá un faltante en hijos en el hogar, asi mismo con la edad y el rango, ya sea del indivudo, padre o madre.

---

## 5. Duplicados
- **Registros duplicados:** 0  

Esto refleja registros únicos de los individuos.

---

## 6. Tipos de Datos
La mayoría de variables son numéricas enteras, seguidas de categóricas. 

---

## 7. Problemas de Codificación
El análisis detecta **columnas con caracteres especiales** producto de problemas de **encoding (UTF-8 / Latin1)**.  
Ejemplos:  
- `"SEGURIDAD Y DEFENSA DE BASES AÃ‰REAS"` (debería ser *AÉREAS*).  
- `"TECNOLÃ“GICO"` (debería ser *TECNOLÓGICO*).  
- `"CON SU PAREJAÂ ;PADRE O MADRE;"`.  

---

## 8. Conclusiones
- La base de datos tiene buena estructura general, sin duplicados, pero presenta **valores faltantes importantes en variables clave** (hijos, personas en el hogar, edades de padres) ya sea por omisión de registro o cuestión social para no diligenciar el dato.
- Existen problemas de codificación en textos que requieren corrección para análisis descriptivos.
- El siguiente paso lógico sería **aplicar imputación de valores faltantes** .