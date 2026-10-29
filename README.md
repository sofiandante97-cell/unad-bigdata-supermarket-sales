# Procesamiento en Batch con PySpark - Big Data (UNAD)

## Descripción de la Solución
Este repositorio contiene el código fuente para el procesamiento en lote (*batch*) de un conjunto de datos de ventas de supermercado (`sales.csv`), utilizando **Apache Spark** mediante DataFrames en un entorno de Google Colab. El script realiza tareas de carga, limpieza de nulos, transformaciones y análisis exploratorio (EDA) para calcular métricas clave de negocio (ingresos por categoría y rendimiento por sucursal).

## Requisitos Previos
* Entorno de ejecución en la nube (Google Colab recomendado).
* Librería PySpark instalada (`pip install pyspark`).
* Conjunto de datos `sales.csv` ubicado en el directorio de trabajo.

## Instrucciones de Ejecución
1. Abra un nuevo cuaderno en **Google Colab**.
2. Instale PySpark ejecutando en una celda:
   ```bash
   !pip install pyspark
3. Suba el archivo de datos sales.csv utilizando el panel lateral de archivos de Google Colab.
4. Cree una celda de código nueva, copie el contenido del archivo batch_analysis.py de este repositorio, péguelo y ejecútelo haciendo clic en el botón de Play (▶️).
5. Visualice las tablas de resultados generadas en la consola de la celda.
