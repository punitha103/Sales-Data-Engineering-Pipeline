from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


PROJECT_PATH = "/path/to/Sales_Data_Engineering"


with DAG(
    dag_id="sales_data_engineering_pipeline",
    start_date=datetime(2026, 8, 16),
    schedule=None,
    catchup=False,
    tags=["sales", "etl", "bronze-silver-gold"],
) as dag:

    data_quality_check = BashOperator(
        task_id="data_quality_check",
        bash_command=f"python3 {PROJECT_PATH}/Scripts/data_quality_check.py",
    )

    bronze_load = BashOperator(
        task_id="bronze_load",
        bash_command=f"python3 {PROJECT_PATH}/Scripts/bronze_load.py",
    )

    silver_transform = BashOperator(
        task_id="silver_transform",
        bash_command=f"python3 {PROJECT_PATH}/Scripts/silver_transform.py",
    )

    gold_transform = BashOperator(
        task_id="gold_transform",
        bash_command=f"python3 {PROJECT_PATH}/Scripts/gold_transform.py",
    )

    data_quality_check >> bronze_load >> silver_transform >> gold_transform