from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

# Create Spark session
spark = SparkSession.builder \
    .appName("Healthcare Bronze to Silver ETL") \
    .getOrCreate()

# Read bronze JSON data
df = spark.read.option("multiline", "true").json(
    "C:/Users/shars/OneDrive/Desktop/Projects/Healthcare Project/Healthcare_cloud_data_platform/data/bronze/patients_raw.json"
)
# Show raw data
print("Bronze Layer Data")
df.show()

# Basic cleaning/transformation
silver_df = df.dropDuplicates(["patient_id"])

silver_df = silver_df.fillna({
    "diagnosis": "UNKNOWN"
})

silver_df = silver_df.withColumn(
    "diagnosis",
    upper(col("diagnosis"))
)

# Show transformed data
print("Silver Layer Data")
silver_df.show()

# Save silver dataset
silver_df.write.mode("overwrite").json(
    "C:/Users/shars/OneDrive/Desktop/Projects/Healthcare Project/Healthcare_cloud_data_platform/data/silver/patients_cleaned"
)

print("Bronze to Silver ETL completed successfully")