import os
import logging
import requests
from pyspark.sql import SparkSession, Row

# =========================
# LOGGING SETUP
# =========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bronze_ingestion")

# =========================
# SPARK SESSION
# =========================
spark = SparkSession.builder \
    .appName("Healthcare_Bronze_Ingestion") \
    .getOrCreate()

# =========================
# BASE PATHS (FIXED)
# =========================
BASE_RAW = r"C:\Users\shars\OneDrive\Desktop\Projects\Healthcare_Project\Healthcare_cloud_data_platform\data\raw"
BASE_BRONZE = r"C:\Users\shars\OneDrive\Desktop\Projects\Healthcare_Project\Healthcare_cloud_data_platform\data\bronze"

# Ensure bronze directory exists
os.makedirs(BASE_BRONZE, exist_ok=True)

# =========================
# FUNCTION: WRITE BRONZE
# =========================
def write_bronze(df, name):
    try:
        output_path = os.path.join(BASE_BRONZE, name)
        df.write.mode("overwrite").parquet(output_path)
        logger.info(f"{name} ingested successfully into Bronze")
    except Exception as e:
        logger.error(f"Failed to ingest {name}: {str(e)}")

# =========================
# 1. PATIENTS (JSON)
# =========================
try:
    patients_path = os.path.join(BASE_RAW, "healthcare_dataset.json")

    patients_df = spark.read.option("multiline", "true").json(patients_path)

    write_bronze(patients_df, "patients")

except Exception as e:
    logger.error(f"Patients ingestion failed: {str(e)}")

# =========================
# 2. CLAIMS (CSV)
# =========================
try:
    claims_path = os.path.join(BASE_RAW, "insurance_claims.csv")

    claims_df = spark.read.option("header", True).option("inferSchema", True).csv(claims_path)

    write_bronze(claims_df, "claims")

except Exception as e:
    logger.error(f"Claims ingestion failed: {str(e)}")

# =========================
# 3. EHR (FHIR JSON)
# =========================
try:
    ehr_path = os.path.join(BASE_RAW, "EHR", "fhir")

    ehr_df = spark.read.option("multiline", "true").json(ehr_path + "\\*")

    write_bronze(ehr_df, "ehr")

except Exception as e:
    logger.error(f"EHR ingestion failed: {str(e)}")

# =========================
# 4. PROVIDERS (CSV FOLDER)
# =========================
try:
    provider_path = os.path.join(BASE_RAW, "Provider")

    provider_df = spark.read.option("header", True).option("inferSchema", True).csv(provider_path + "\\*")

    write_bronze(provider_df, "providers")

except Exception as e:
    logger.error(f"Provider ingestion failed: {str(e)}")

# =========================
# 5. FRAUD DATA
# =========================
try:
    fraud_path = os.path.join(BASE_RAW, "Fraud")

    fraud_df = spark.read.option("header", True).option("inferSchema", True).csv(fraud_path + "\\*")

    write_bronze(fraud_df, "fraud")

except Exception as e:
    logger.error(f"Fraud ingestion failed: {str(e)}")

# =========================
# 6. API INGESTION (SAFE VERSION)
# =========================
try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        api_df = spark.createDataFrame([Row(**x) for x in data])

        write_bronze(api_df, "api_patients")

        logger.info("API ingestion successful")
    else:
        logger.warning("API returned non-200 response, skipping")

except Exception as e:
    logger.warning(f"API ingestion skipped: {str(e)}")

# =========================
# DONE
# =========================
logger.info("Bronze ingestion pipeline completed")