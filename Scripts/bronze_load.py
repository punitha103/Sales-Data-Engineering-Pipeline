import shutil
from pathlib import Path

# Project root folder
project_root = Path(__file__).resolve().parent.parent

source_file = project_root / "Data" / "Raw" / "sales_dataset.csv"
bronze_file = project_root / "Bronze" / "sales_dataset_bronze.csv"

bronze_file.parent.mkdir(exist_ok=True)

shutil.copy2(source_file, bronze_file)

print("Raw data successfully loaded into Bronze Layer")
print("Bronze file:", bronze_file)