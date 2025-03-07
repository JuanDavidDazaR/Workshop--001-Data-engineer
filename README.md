# Workshop--001-Data-engineer
This project is part of a Data Engineer exercise. Its objective is to demonstrate skills in data management, transformation and visualization using Python, PostgreSQL and Jupyter Notebook.  Starting from a CSV file with 50,000 records about candidates in selection processes.

# Data Engineering and EDA Project

**Por Juan Dvaid Daza**

## Visión General
Este proyecto explora un conjunto de datos utilizando técnicas de **Ingeniería de Datos** y **Análisis Exploratorio de Datos (EDA)**. Se han empleado herramientas como **Python, PostgreSQL y Power BI** para transformar y visualizar la información de manera efectiva.

El propósito principal es analizar la estructura del conjunto de datos, identificar patrones relevantes y evaluar la calidad de los datos para su uso en la toma de decisiones.

## Objetivos Clave
- Implementar un proceso ETL eficiente para manejo de datos.
- Realizar limpieza y transformación de los datos.
- Explorar patrones y relaciones en los datos, incluyendo:
  - Análisis de patrones de contratación.
  - Identificación de anomalías en los datos.
  - Relación entre la antigüedad y la experiencia de los empleados.
- Crear visualizaciones claras y efectivas en Power BI para comunicar hallazgos clave.

## Tecnologías Utilizadas
- **Python**: Procesamiento y análisis de datos.
- **Jupyter Notebook**: Análisis interactivo.
- **PostgreSQL**: Gestión y almacenamiento de bases de datos.
- **Power BI**: Creación de dashboards y visualizaciones.

## Tabla de Contenidos
1. Prerrequisitos
2. Instalación
   - Configuración del entorno virtual de Python
   - Configuración de PostgreSQL
3. Uso
4. Integración con Power BI
5. Documentación

## Prerrequisitos
Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:
- **Python**: 3.12.9
- **PostgreSQL**: 14+
- **Power BI Desktop** para visualización
- **Visual Studio Code** o tu IDE de Python preferido

## Instalación

### Clonar el repositorio
```sh
git clone https://github.com/JuanDavidDazaR/Workshop--001-Data-engineer.git
```
## Configuración del Entorno Virtual
### Crear y activar entorno virtual
```sh
python -m venv venv
```
**Windows (CMD):**
```sh
venv\Scripts\activate.bat
```
**Windows (PowerShell):**
```sh
venv\Scripts\Activate.ps1
```
**Mac/Linux:**
```sh
source venv/bin/activate
```
### Instalar dependencias en el entorno virtual
```sh
pip install -r requirements.txt
```

## Configuración de PostgreSQL
1. Crea una base de datos PostgreSQL (por ejemplo, `project_db`).
2. Configura las variables de entorno en un archivo `.env`:
```sh
PG_USER=tu_usuario_postgres
PG_PASSWORD=tu_contraseña_postgres
PG_HOST=localhost_o_host_remoto
PG_PORT=5432
PG_DATABASE=project_db
```
3. Asegúrate de que la estructura de la base de datos coincida con los datos analizados.

## Uso
### Ejecutar el script ETL para cargar datos en PostgreSQL
```sh
python main.py
```

## Integración con Power BI
### Conéctate a PostgreSQL
1. Abre **Power BI Desktop**.
2. Selecciona **Obtener datos > Base de datos de PostgreSQL**.
3. Ingresa los detalles de conexión:
   - **Servidor**: `tu_host_postgres`
   - **Base de datos**: `project_db`
   - **Autenticación**: Nombre de usuario/Contraseña
   - **Usuario**: `PG_USER` desde `.env`
   - **Contraseña**: `PG_PASSWORD` desde `.env`
4. Carga los datos y crea visualizaciones interactivas.

## Ejemplos de Gráficos en Power BI
- **Distribución de empleados según experiencia**
- **Tendencias en patrones de contratación**
- **Análisis de calidad de los datos y detección de anomalías**

---
Este README proporciona una guía estructurada para configurar y ejecutar el análisis de datos, facilitando su implementación y replicación. 🚀
