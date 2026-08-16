import pandas as pd

# Read raw data
file_path = r"C:\Users\acer\OneDrive\Desktop\Sales_Data_Engineering\Data\Raw\sales_dataset.csv"

df = pd.read_csv(file_path)

print("========== DATA QUALITY REPORT ==========")

# 1. Row and column count
print("\n1. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Null value check
print("\n2. Null Value Check:")
null_values = df.isnull().sum()
print(null_values[null_values > 0])

# 3. Duplicate record check
print("\n3. Duplicate Record Check:")
duplicates = df.duplicated().sum()
print("Duplicate Records:", duplicates)

# 4. Data type check
print("\n4. Data Types:")
print(df.dtypes)

# 5. Negative Sales Amount check
print("\n5. Negative Sales Amount Check:")
if "Sales_Amount" in df.columns:
    negative_sales = (df["Sales_Amount"] < 0).sum()
    print("Negative Sales Amount:", negative_sales)

# 6. Quantity validation
print("\n6. Quantity Check:")
if "Quantity_Sold" in df.columns:
    invalid_quantity = (df["Quantity_Sold"] <= 0).sum()
    print("Invalid Quantity:", invalid_quantity)

# 7. Missing column check
print("\n7. Required Column Check:")

required_columns = [
    "Product_ID",
    "Sale_Date",
    "Sales_Rep",
    "Region",
    "Sales_Amount",
    "Quantity_Sold",
    "Product_Category"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print("Missing Columns:", missing_columns)
else:
    print("All required columns are available.")

print("\n========== DATA QUALITY CHECK COMPLETED ==========")