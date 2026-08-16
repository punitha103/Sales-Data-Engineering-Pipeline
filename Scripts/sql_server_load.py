import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# Project path
project_root = Path(__file__).resolve().parent.parent

# Gold folder
gold_folder = project_root / "Gold"

# SQL Server connection
server = "localhost"
database = "SalesDataWarehouse"

connection_string = (
    "mssql+pyodbc://@"
    + server
    + "/"
    + database
    + "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Gold files
tables = {
    "dim_product.csv": "Dim_Product",
    "dim_date.csv": "Dim_Date",
    "dim_sales_rep.csv": "Dim_Sales_Rep",
    "dim_region.csv": "Dim_Region",
    "fact_sales.csv": "Fact_Sales"
}

for file_name, table_name in tables.items():

    file_path = gold_folder / file_name

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded successfully")

print("All Gold tables loaded into SQL Server!")