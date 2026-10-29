from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum, count

# 1. Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("SupermarketSalesBatchAnalysis") \
    .getOrCreate()

# 2. Cargar tu archivo sales.csv
file_path = "sales.csv"  
df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)

# 3. Limpieza de datos
df_cleaned = df.dropna()

# 4. Transformaciones y Análisis (EDA): Ventas Totales por Categoría de Producto
print("\n--- Análisis: Ingresos Totales por Categoría de Producto ---")
sales_by_category = df_cleaned.groupBy("product_category") \
    .agg(
        sum("total_price").alias("Ingresos_Totales"),
        avg("unit_price").alias("Precio_Promedio"),
        count("sale_id").alias("Total_Transacciones")
    ) \
    .orderBy(col("Ingresos_Totales").desc())

sales_by_category.show(truncate=False)

# 5. Análisis por Sucursal (Branch)
print("\n--- Análisis: Rendimiento por Sucursal ---")
sales_by_branch = df_cleaned.groupBy("branch") \
    .agg(sum("total_price").alias("Ingresos_Sucursal")) \
    .orderBy(col("Ingresos_Sucursal").desc())

sales_by_branch.show()
