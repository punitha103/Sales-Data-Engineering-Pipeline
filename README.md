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