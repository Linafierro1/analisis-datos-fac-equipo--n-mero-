# 📊 Proyecto Colaborativo: Análisis de Datos FAC - Bienestar Familiar

## 🎯 Objetivo
Realizar un análisis básico de datos reales de la encuesta de **bienestar familiar del personal de la Fuerza Aérea Colombiana (FAC)**, aplicando trabajo colaborativo con **Git/GitHub** y herramientas de análisis de datos en Python.

## 👥 Organización del Equipo
- **Estudiante A**: Líder de análisis demográfico  
- **Estudiante B**: Especialista en datos familiares  
- **Estudiante C**: Experto en calidad de datos  

Repositorio: `analisis-datos-fac-equipo-[número]`

## 📂 Estructura del Proyecto
analisis-datos-fac-equipo-X/
├── 📄 README.md # Descripción general del proyecto
├── 📄 datos_exploracion.py # Archivo principal integrado
├── 📄 resultados_analisis.md # Reporte conjunto del equipo
├── 📁 datos/
│ └── 📄 JEFAB_2024.xlsx # Base de datos original (6.424 registros, 261 variables)
└── 📁 reportes/
├── 📄 demografia_basica.md # Reporte Estudiante A
├── 📄 analisis_familiar.md # Reporte Estudiante B
└── 📄 calidad_datos.md # Reporte Estudiante C

## 🚀 Tareas por Estudiante
### 👤 Estudiante A: Análisis Demográfico
- Explorar edad, género y grado militar  
- Visualizaciones simples de distribución  
- Responder:
  1. ¿Cuál es el rango de edad más común?  
  2. ¿Existen diferencias por género?  
  3. ¿Cuál es el grado militar más frecuente?  

### 👤 Estudiante B: Análisis Familiar
- Analizar estado civil, hijos y convivencia  
- Identificar patrones familiares  
- Responder:  
  1. ¿Qué porcentaje del personal está casado?  
  2. ¿Cuántos tienen hijos y conviven con ellos?  
  3. ¿Hay relación entre edad y estado civil?  

### 👤 Estudiante C: Calidad de Datos
- Identificar datos faltantes, duplicados y problemas de encoding  
- Proponer estrategias de limpieza  
- Responder:  
  1. ¿Qué columnas tienen más datos faltantes?  
  2. ¿Cuántos registros están duplicados?  
  3. ¿Qué problemas de codificación existen?  

## 🔄 Flujo de Trabajo Colaborativo
- **Semana 1**: Configuración y exploración individual  
- **Semana 2**: Integración, documentación y reporte conjunto  

### Comandos Git básicos
```bash
# Configuración inicial
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Flujo de trabajo
git status
git pull
git add archivo.py
git commit -m "mensaje"
git push

# Verificación
git log --oneline
git remote -v
