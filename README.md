# 🏥 Healthcare Cloud Data Platform: End-to-End Healthcare Analytics & Intelligence

## Transforming Healthcare Data into Actionable Insights

Healthcare organizations generate massive volumes of data every day—from patient encounters and insurance claims to provider networks, EHR systems, fraud monitoring platforms, and external healthcare services. While these datasets hold immense value, they often exist in disconnected systems, making it difficult to derive meaningful insights that improve patient outcomes and operational efficiency.

This project demonstrates the design and implementation of a modern Healthcare Cloud Data Platform that consolidates multiple healthcare data sources into a scalable analytics ecosystem. Using PySpark, Medallion Architecture principles, Parquet storage, and Power BI, this solution transforms fragmented healthcare data into business-ready intelligence for clinical, financial, and operational stakeholders.

---

## 🎯 Project Vision

The objective of this platform is to simulate a real-world healthcare analytics environment capable of:

* Ingesting data from diverse healthcare systems
* Standardizing healthcare datasets for analytics consumption
* Creating a scalable foundation for future data warehousing solutions
* Delivering executive-level insights through interactive dashboards
* Supporting data-driven decision-making across healthcare operations

Rather than analyzing a single dataset, this project focuses on building the foundational data platform that powers healthcare analytics.

---

# 🏗️ Solution Architecture

```text
Healthcare Data Sources
        │
        ▼
PySpark Ingestion Framework
        │
        ▼
Bronze Layer (Raw Parquet Storage)
        │
        ▼
Analytics Dataset
        │
        ▼
Power BI Executive Dashboard
```

The architecture follows modern Lakehouse and Medallion Architecture principles commonly adopted across healthcare organizations and cloud data platforms.

---

# 🚀 Technology Stack

### Data Engineering

* Python
* PySpark
* Parquet
* JSON
* CSV
* REST APIs

### Analytics & Visualization

* Power BI

### Development & Version Control

* Git
* GitHub
* Visual Studio Code

### Healthcare Standards

* FHIR (Fast Healthcare Interoperability Resources)

---

# 📂 Healthcare Data Sources

A key objective of this project was to simulate the diversity of data encountered within modern healthcare ecosystems.

---

## 1️⃣ Patient Clinical Dataset

### File

```text
healthcare_dataset.json
```

### Purpose

Contains patient-level demographic and clinical information including:

* Patient ID
* Age
* Gender
* Diagnosis
* Associated Provider

### Why This Dataset Matters

Patient records serve as the foundation for virtually all healthcare analytics initiatives. They enable disease analysis, demographic segmentation, care management, and provider attribution.

---

## 2️⃣ Insurance Claims Dataset

### File

```text
insurance_claims.csv
```

### Purpose

Captures claim transactions and healthcare reimbursement activity.

### Why This Dataset Matters

Claims data represents one of the most critical financial assets in healthcare analytics. Understanding reimbursement patterns helps organizations evaluate payer performance, control costs, and identify revenue opportunities.

---

## 3️⃣ Electronic Health Records (FHIR)

### Source

```text
EHR/fhir/
```

### Purpose

FHIR-based clinical records containing healthcare encounter information.

### Why This Dataset Matters

FHIR has become the industry standard for healthcare interoperability. Incorporating FHIR demonstrates familiarity with healthcare-specific data standards used throughout hospitals, payers, and healthcare technology organizations.

---

## 4️⃣ Provider Dataset

### Source

```text
Provider/
```

### Purpose

Contains provider and hospital-related information.

### Why This Dataset Matters

Provider analytics enable organizations to evaluate utilization patterns, operational performance, and patient distribution across healthcare networks.

---

## 5️⃣ Healthcare Fraud Dataset

### Source

```text
Fraud/
```

### Purpose

Contains healthcare transaction records used for fraud analytics.

### Why This Dataset Matters

Fraud prevention remains a significant focus area for healthcare organizations due to the substantial financial losses associated with fraudulent claims activity.

---

## 6️⃣ External API Data

### Source

REST API Integration

### Purpose

Simulates ingestion of external healthcare services and third-party systems.

### Why This Dataset Matters

Modern healthcare ecosystems increasingly rely on APIs for exchanging patient, provider, and operational data across platforms.

---

# ⚙️ Bronze Layer Data Engineering Pipeline

The Bronze Layer serves as the system of record for all incoming healthcare data.

Using PySpark, raw datasets are ingested and persisted into Parquet format without applying business transformations. This approach preserves source fidelity while enabling scalable downstream analytics.

### Datasets Ingested

| Dataset      | Source Type |
| ------------ | ----------- |
| Patients     | JSON        |
| Claims       | CSV         |
| EHR          | FHIR JSON   |
| Providers    | CSV         |
| Fraud        | CSV         |
| API Patients | REST API    |

### Why Parquet?

Parquet was selected because it is:

* Highly compressed
* Columnar by design
* Optimized for analytical workloads
* Widely adopted in Databricks, Snowflake, Azure, and AWS environments

---

# 📊 Executive Analytics Dashboard

The Power BI dashboard was intentionally designed to answer three strategic healthcare business questions frequently encountered by healthcare administrators, finance leaders, and operations teams.

---

## 💰 Insurance Provider Analysis

### Visualization

Pie Chart

### Business Question

**Which insurance providers account for the highest healthcare claim expenditures?**

### Metrics

* Total Claim Amount

### Why This Visualization?

Insurance providers represent a finite set of reimbursement entities. A pie chart effectively highlights claim concentration and reveals which providers contribute the largest share of total healthcare costs.

### Business Value

This analysis helps stakeholders:

* Understand payer mix
* Evaluate reimbursement concentration
* Assess financial exposure to specific insurance providers
* Support contract negotiations

---

## 🩺 Medical Condition Cost Analysis

### Visualization

Area Chart

### Business Question

**Which medical conditions generate the highest healthcare spending?**

### Metrics

* Average Billing
* Total Billing
* Patient Count

### Why This Visualization?

Medical conditions are among the strongest drivers of healthcare expenditure. The area chart highlights cost distribution across disease categories while revealing overall spending trends.

### Business Value

This analysis enables healthcare leaders to:

* Identify high-cost disease groups
* Prioritize care management initiatives
* Support population health strategies
* Allocate clinical resources more effectively

### Additional Insight

Tooltips were incorporated to provide:

* Patient Volume
* Total Billing Amount

This helps distinguish between:

* Conditions affecting many patients
* Conditions generating disproportionately high costs

---

## 🏥 Hospital Admissions vs Billing Analysis

### Visualization

Clustered Bar Chart

### Business Question

**How do hospital admission volumes compare with average billing performance?**

### Metrics

* Admissions
* Average Billing

### Why This Visualization?

Hospitals differ significantly in patient volume and cost structures. Comparing admissions alongside billing metrics helps identify facilities that may be operating under unique cost or utilization patterns.

### Business Value

This dashboard supports:

* Capacity planning
* Financial benchmarking
* Operational performance evaluation
* Resource allocation decisions

---

# 🔍 Key Insights Delivered

Through this platform, stakeholders can:

✔ Analyze healthcare spending by insurance provider

✔ Identify costly medical conditions

✔ Compare hospital utilization patterns

✔ Monitor financial performance indicators

✔ Support strategic healthcare planning

✔ Establish a scalable analytics foundation

---

# 🌟 Future Enhancements

The next evolution of this platform includes:

* Silver Layer transformation pipelines
* Gold Layer business metrics
* Snowflake integration
* Databricks workflow orchestration
* Azure Data Lake Storage
* Healthcare fraud detection models
* Data quality validation framework
* Automated pipeline scheduling using Airflow or Prefect

---

# 📚 Skills Demonstrated

This project showcases expertise across:

* Healthcare Data Engineering
* PySpark Development
* Medallion Architecture
* Healthcare Data Standards (FHIR)
* API Integration
* Data Lake Design
* Parquet Optimization
* Power BI Analytics
* Cloud Data Platform Concepts
* End-to-End Data Pipeline Development

---

# 👨‍💻 Author

**Sri Harsha Chittapragada**

Analytics Engineer | Data Engineer

Passionate about building scalable healthcare analytics platforms that transform raw healthcare data into meaningful business intelligence through modern data engineering practices.
