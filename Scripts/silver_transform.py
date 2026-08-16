import pandas as pd
from pathlib import Path

# Project root folder
project_root = Path(__file__).resolve().parent.parent

# Bronze input
bronze_file = project_root / "Bronze" / "sales_dataset_bronze.csv"

# Read Bronze data
df = pd.read_csv(bronze_file)

print("Bronze data loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFirst 5 records:")
print(df.head())



# Check null values
print("\nNull values before cleaning:")
print(df.isnull().sum())

# Remove duplicate records
duplicate_count = df.duplicated().sum()
print("\nDuplicate records:", duplicate_count)

df = df.drop_duplicates()

print("\nDuplicates removed.")
print("Rows after cleaning:", len(df))


# Convert Sale_Date to datetime
df["Sale_Date"] = pd.to_datetime(
    df["Sale_Date"],
    errors="coerce"
)

# Convert numeric columns to numeric data types
numeric_columns = [
    "Sales_Amount",
    "Quantity_Sold",
    "Unit_Cost"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

print("\nData types after transformation:")
print(df.dtypes)


# Check invalid Sales Amount
if "Sales_Amount" in df.columns:
    invalid_sales = (df["Sales_Amount"] < 0).sum()
    print("\nInvalid Sales Amount:", invalid_sales)

    # Remove negative sales
    df = df[df["Sales_Amount"] >= 0]


# Check invalid Quantity
if "Quantity_Sold" in df.columns:
    invalid_quantity = (df["Quantity_Sold"] <= 0).sum()
    print("Invalid Quantity:", invalid_quantity)

    # Remove zero or negative quantity
    df = df[df["Quantity_Sold"] > 0]


print("\nRows after invalid value cleaning:", len(df))


# Save cleaned data to Silver Layer
silver_file = project_root / "Silver" / "sales_dataset_silver.csv"

silver_file.parent.mkdir(exist_ok=True)

df.to_csv(silver_file, index=False)

print("\nSilver data saved successfully!")
print("Silver file:", silver_file)