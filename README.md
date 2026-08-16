# Sales Data Engineering Pipeline

## 📌 Project Overview

This project implements an end-to-end Sales Data Engineering Pipeline to ingest, validate, clean, transform, and prepare sales data for analytics.

The pipeline follows a **Bronze → Silver → Gold** data architecture and uses Python, PySpark, SQL Server, and Airflow for data processing and workflow orchestration.

## 🏗️ Data Flow

Raw Sales Data
      ↓
   Bronze
      ↓
   Silver
      ↓
    Gold
      ↓
 SQL Server
      ↓
 Power BI


 ## 🛠️ Technologies Used

- Python
- PySpark
- SQL Server
- Apache Airflow
- SQL
- Power BI
- Git & GitHub

## 🔄 Pipeline Layers

### Bronze Layer
- Stores raw source data.
- Preserves the original data for traceability.

### Silver Layer
- Cleans and transforms the raw data.
- Handles missing values and duplicate records.
- Applies data validation and transformation rules.

### Gold Layer
- Contains business-ready transformed data.
- Creates Fact and Dimension tables.
- Optimized for reporting and analytics.

## ✅ Data Quality Checks

The pipeline performs the following data quality checks:

- Null value validation
- Duplicate record detection
- Data type validation
- Required column validation
- Invalid record identification
- Record count validation
- Primary key uniqueness checks

## ⚙️ Workflow Orchestration

Apache Airflow is used to orchestrate the data pipeline and automate the execution of ETL tasks.

The workflow manages tasks such as:

1. Extract raw sales data
2. Validate source data
3. Process data using PySpark
4. Load transformed data
5. Perform data quality checks
6. Prepare data for analytics


## 📂 Project Structure

```text
Sales_Data_Engineering/
│
├── Data/
│   └── Raw/
│
├── Bronze/
│   └── Raw processed data
│
├── Silver/
│   └── Cleaned and transformed data
│
├── Gold/
│   ├── Fact tables
│   └── Dimension tables
│
├── Scripts/
│   ├── csv_validation.py
│   ├── pyspark_transform.py
│   └── sql_server_load.py
│
├── SQL/
│   └── SQL scripts
│
├── Airflow/
│   └── DAG files
│
├── PowerBI/
│   └── Dashboard files/screenshots
│
└── README.md
```

## 🎯 Key Features

- End-to-end ETL pipeline
- Bronze → Silver → Gold architecture
- PySpark data transformation
- SQL Server data storage
- Apache Airflow workflow orchestration
- Data quality checks
- Fact and Dimension table design
- Power BI-ready analytical data

## 🏗️ Architecture Diagram

```text
                 ┌─────────────────┐
                 │   Raw CSV Data  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Bronze Layer   │
                 │   Raw Data      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Silver Layer   │
                 │ Clean & Transform│
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Gold Layer    │
                 │ Fact & Dimension│
                 │     Tables      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   SQL Server    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Power BI     │
                 │    Dashboard    │
                 └─────────────────┘

              Apache Airflow
          Workflow Orchestration
```      

## 🔄 ETL Workflow

The sales data pipeline follows these steps:

1. **Extract** – Collect raw sales data from CSV files.
2. **Validate** – Validate columns, data types, null values, and duplicate records using Python.
3. **Bronze Layer** – Store the raw data without major transformations.
4. **Transform** – Clean and transform the data using PySpark.
5. **Silver Layer** – Store cleaned and standardized data.
6. **Gold Layer** – Create business-ready Fact and Dimension tables.
7. **Load** – Load the processed data into SQL Server.
8. **Orchestrate** – Use Apache Airflow to automate and monitor pipeline tasks.
9. **Visualize** – Connect Power BI to the analytical data for reporting.

### 📊 Data Flow

```text
Raw CSV
   ↓
Python Validation
   ↓
Bronze Layer
   ↓
PySpark Transformation
   ↓
Silver Layer
   ↓
Gold Layer
   ↓
SQL Server
   ↓
Power BI
```

## 🗄️ Data Warehouse Design

The Gold layer follows a **Star Schema** design.

### Dimension Tables

- `dim_product` – Product information
- `dim_date` – Date-related attributes
- `dim_sales_rep` – Sales representative information
- `dim_region` – Region information

### Fact Table

- `fact_sales` – Stores sales transactions and measurable business metrics

### 📊 Star Schema

```text
                  dim_product
                       │
                       │
dim_date ─────── fact_sales ─────── dim_sales_rep
                       │
                       │
                  dim_region
```

## 📈 Project Outcome

- Built an end-to-end sales data engineering pipeline.
- Implemented Bronze, Silver, and Gold data layers.
- Performed data validation and transformation using Python and PySpark.
- Designed a Star Schema with Fact and Dimension tables.
- Loaded analytical data into SQL Server.
- Automated pipeline workflows using Apache Airflow.
- Prepared business-ready data for Power BI reporting and analytics.

## ▶️ How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/punitha103/Sales-Data-Engineering-Pipeline.git
cd Sales-Data-Engineering-Pipeline
```
### Step 2 — Install Required Python Libraries

```bash
pip install pandas pyspark
```

### Step 3 — Run Data Validation
```bash
python Scripts/csv_validation.py
```

### Step 4 — Run PySpark Transformation
```bash
python Scripts/pyspark_transform.py
```

### Step 5 — Load Data into SQL Server
```bash
python Scripts/sql_server_load.py
```

### Step 6 — Run Airflow

Start Airflow and run the project DAG from the Airflow UI.

### Step 7 — View the Dashboard

Open the Power BI dashboard and refresh the data.


## 👩‍💻 Author

###  Punitha S

## 🚀 Aspiring Data Engineer

💻 Python | ⚡ PySpark | 🗄️ SQL | 🔄 Apache Airflow | 📊 Power BI
