# Resultados relevantes
---
## Introducción

El presente proyecto académico se desarrolla a partir de la **Encuesta de Bienestar Familiar aplicada al personal de la FAC**, contenida en el archivo `JEFAB_2024.xlsx`, que integra información de **6.423 registros** y **231 variables**. 
El análisis de este conjunto de datos no solo permite practicar técnicas estadísticas y de programación, sino también comprender el impacto social de los hallazgos.

Desde la perspectiva educativa, el profesor plantea este ejercicio con el fin de que los estudiantes:
- Aprendan a manejar datos reales en **Python (pandas, matplotlib)**.  
- Trabajen en equipo utilizando **Git/GitHub**.  
- Produzcan reportes claros en **Markdown**.  
- Reflexionen sobre el papel de la estadística como soporte en la toma de decisiones sociales e institucionales.  

De esta forma, se integran competencias técnicas y trabajo colaborativo con una mirada social de los datos.


## Antecedentes Históricos

La **Fuerza Aérea Colombiana (FAC)**, en cumplimiento de su misión de proteger la soberanía aérea del país, ha reconocido la importancia del **bienestar de su personal y sus familias** como un factor clave para el desempeño institucional. 
En este marco, desde el **Plan General de Bienestar y Familia (PGBF)** se han diseñado iniciativas de apoyo integral, buscando fortalecer la calidad de vida, cohesión familiar y satisfacción laboral de sus miembros.

Con el tiempo, la necesidad de contar con información confiable llevó a la creación de la **Encuesta de Bienestar Familiar (JEFAB)**, instrumento aplicado a nivel institucional que recopila datos sobre demografía, educación, condiciones familiares, vivienda, salud y entorno social.

Este levantamiento de información se ha consolidado como una herramienta esencial para **diagnosticar la realidad del personal** y diseñar políticas de bienestar con base en evidencia.

## Finalidad Social de la Encuesta

La **Encuesta de Bienestar Familiar** se realiza con el propósito de:

1. **Diagnóstico institucional** → Identificar necesidades reales del personal y sus familias.  
2. **Diseño de políticas de bienestar** → Orientar recursos en programas de apoyo educativo, familiar, social y económico.  
3. **Fortalecimiento de la cohesión familiar** → Mejorar la relación entre el entorno militar y el núcleo familiar.  
4. **Seguimiento y evaluación** → Medir el impacto de las políticas implementadas a lo largo del tiempo.  
5. **Aplicación académica** → Servir como caso real para la formación en estadística, análisis de datos y colaboración en proyectos.  

## Análisis de Calidad de Datos
El análisis de la base **JEFAB_2024.xlsx** (6.423 registros y 231 variables) mostró que la estructura de los datos es consistente, sin duplicados, pero con **19.831 valores faltantes** concentrados en variables clave como número de hijos, personas en el hogar y edades de padres; el script `calidad_datos.py` corrige automáticamente valores relacionados con hijos, convierte variables categóricas para optimizar el análisis y genera una nueva versión de la base limpia, aunque persisten problemas de **codificación de caracteres** que afectan algunas variables de texto; en conclusión, la base es sólida para análisis, pero requiere imputación de faltantes o selección de variables con poca presencia de faltantes y corrección de encoding antes de avanzar a etapas analíticas más complejas.


---
## Análisis Demográfico

La población analizada de la FAC está conformada mayoritariamente por **hombres (≈69%)** frente a un **31% de mujeres**, con una **edad promedio de 36,7 años** y un rango etario predominante entre **33–37 años** en ambos géneros. Aunque la moda es compartida, la distribución revela diferencias: los hombres se concentran más en tramos jóvenes e intermedios (18–37 años), mientras que las mujeres presentan mayor peso relativo en edades medias y avanzadas (43–52 y algunos casos mayores de 58 años). En cuanto al **grado militar**, al excluir la categoría “No responde”, en hombres predominan los **suboficiales técnicos (T1, T2, T3)**, mientras que en mujeres se observa una participación más equilibrada, con presencia destacada de **oficiales en grados iniciales (CT, TE, ST)**. Esto refleja contrastes tanto en la estructura etaria como en la composición jerárquica por género.

## Análisis Familiar


La población analizada está compuesta mayoritariamente por personas casadas (≈61%), seguidas por solteros (≈32%), mientras que los estados civiles asociados a rupturas como separados, divorciados y viudos representan un porcentaje menor, aunque con dinámicas relevantes. La edad promedio varía según estado civil: los solteros rondan los 30 años, en contraste con los casados y divorciados que se ubican cerca de los 40, y los viudos que alcanzan los 47 años en promedio, reflejando un ciclo de vida vinculado al estado civil. En cuanto a la estructura familiar, un 57% de los encuestados reporta tener hijos, concentrándose principalmente en 1 o 2 descendientes, aunque se observa que a mayor número de hijos aumenta la proporción de maltrato intrafamiliar, pasando de 3,4% en quienes no tienen hijos a cerca del 8% en familias con 4 hijos. Aunque la incidencia global de maltrato intrafamiliar es de apenas 4,7%, este valor se eleva en subgrupos específicos: separados (16,7%), divorciados (13,2%) y viudos (12,8%), frente a cifras mucho menores en casados y solteros. Esto sugiere que la combinación de rupturas conyugales, edad y número de hijos constituye un escenario de mayor vulnerabilidad frente a la violencia intrafamiliar.
