import pandas as pd
from pathlib import Path

# Project location
project_root = Path(__file__).resolve().parent.parent

# Read Silver data
silver_file = project_root / "Silver" / "sales_dataset_silver.csv"

df = pd.read_csv(silver_file)

print("Silver data loaded successfully")

# Convert Sale_Date
df["Sale_Date"] = pd.to_datetime(
    df["Sale_Date"],
    errors="coerce"
)

# Create Product Dimension
dim_product = df[
    ["Product_ID", "Product_Category"]
].drop_duplicates()

# Create Product Key
dim_product.insert(
    0,
    "Product_Key",
    range(1, len(dim_product) + 1)
)

print("\nDim_Product:")
print(dim_product)


# Create Date Dimension

dim_date = df[["Sale_Date"]].drop_duplicates().copy()

# Create Date Key
dim_date["Date_Key"] = (
    dim_date["Sale_Date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

# Create date attributes
dim_date["Year"] = dim_date["Sale_Date"].dt.year
dim_date["Month"] = dim_date["Sale_Date"].dt.month
dim_date["Month_Name"] = dim_date["Sale_Date"].dt.month_name()
dim_date["Day"] = dim_date["Sale_Date"].dt.day
dim_date["Day_Name"] = dim_date["Sale_Date"].dt.day_name()

# Arrange columns
dim_date = dim_date[
    [
        "Date_Key",
        "Sale_Date",
        "Year",
        "Month",
        "Month_Name",
        "Day",
        "Day_Name"
    ]
]

print("\nDim_Date:")
print(dim_date.head())


# Create Sales Representative Dimension

dim_sales_rep = df[["Sales_Rep"]].drop_duplicates().copy()

# Create Sales Rep Key
dim_sales_rep.insert(
    0,
    "Sales_Rep_Key",
    range(1, len(dim_sales_rep) + 1)
)

print("\nDim_Sales_Rep:")
print(dim_sales_rep)


# Create Region Dimension

dim_region = df[["Region"]].drop_duplicates().copy()

# Create Region Key
dim_region.insert(
    0,
    "Region_Key",
    range(1, len(dim_region) + 1)
)

print("\nDim_Region:")
print(dim_region)

# Create Fact Sales table

fact_sales = df.copy()

# Add Product Key
fact_sales = fact_sales.merge(
    dim_product[["Product_Key", "Product_ID"]],
    on="Product_ID",
    how="left"
)

# Add Date Key
fact_sales = fact_sales.merge(
    dim_date[["Date_Key", "Sale_Date"]],
    on="Sale_Date",
    how="left"
)

# Add Sales Rep Key
fact_sales = fact_sales.merge(
    dim_sales_rep[["Sales_Rep_Key", "Sales_Rep"]],
    on="Sales_Rep",
    how="left"
)

# Add Region Key
fact_sales = fact_sales.merge(
    dim_region[["Region_Key", "Region"]],
    on="Region",
    how="left"
)

# Select Fact table columns
fact_sales = fact_sales[
    [
        "Product_Key",
        "Date_Key",
        "Sales_Rep_Key",
        "Region_Key",
        "Sales_Amount",
        "Quantity_Sold",
        "Unit_Cost",
        "Unit_Price",
        "Discount"
    ]
]

# Create Sales Key
fact_sales.insert(
    0,
    "Sales_Key",
    range(1, len(fact_sales) + 1)
)

print("\nFact_Sales:")
print(fact_sales.head())

print("\nFact Sales Rows:", len(fact_sales))

# Create Gold folder
gold_folder = project_root / "Gold"
gold_folder.mkdir(exist_ok=True)

# Save Dimension tables
dim_product.to_csv(
    gold_folder / "dim_product.csv",
    index=False
)

dim_date.to_csv(
    gold_folder / "dim_date.csv",
    index=False
)

dim_sales_rep.to_csv(
    gold_folder / "dim_sales_rep.csv",
    index=False
)

dim_region.to_csv(
    gold_folder / "dim_region.csv",
    index=False
)

# Save Fact table
fact_sales.to_csv(
    gold_folder / "fact_sales.csv",
    index=False
)

print("\nAll Gold tables saved successfully!")