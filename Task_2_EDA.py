import pandas as pd
import os

# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(
    BASE_DIR,
    "01_Dataset",
    "ApexPlanet_Cleaned_Dataset.xlsx"
)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_excel(dataset_path)

print("=" * 60)
print("APEXPLANET TASK 2 - EDA & BUSINESS INTELLIGENCE")
print("=" * 60)


# ============================================================
# 3. DATASET OVERVIEW
# ============================================================

print("\n--- DATASET OVERVIEW ---")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# ============================================================
# 4. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("--- DESCRIPTIVE STATISTICS ---")
print("=" * 60)

print(df.describe())


# ============================================================
# 5. NUMERICAL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("--- NUMERICAL ANALYSIS ---")
print("=" * 60)


numerical_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

for column in numerical_columns:

    print("\n" + "-" * 50)
    print(column)
    print("-" * 50)

    print("Mean:", df[column].mean())
    print("Median:", df[column].median())
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())
    print("Standard Deviation:", df[column].std())


# ============================================================
# 6. CATEGORICAL ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("--- CATEGORICAL ANALYSIS ---")
print("=" * 60)


categorical_columns = [
    "Gender",
    "City",
    "Product",
    "Category"
]

for column in categorical_columns:

    print("\n" + "-" * 50)
    print(column)
    print("-" * 50)

    print(df[column].value_counts())


# ============================================================
# 7. BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("--- KEY BUSINESS INSIGHTS ---")
print("=" * 60)


# Highest selling product by number of orders
top_product = df["Product"].value_counts().idxmax()
top_product_orders = df["Product"].value_counts().max()

print(
    f"\n1. Most frequently ordered product: "
    f"{top_product} ({top_product_orders} orders)"
)


# Highest order category
top_category = df["Category"].value_counts().idxmax()
top_category_orders = df["Category"].value_counts().max()

print(
    f"2. Most frequently ordered category: "
    f"{top_category} ({top_category_orders} orders)"
)


# City with highest number of orders
top_city = df["City"].value_counts().idxmax()
top_city_orders = df["City"].value_counts().max()

print(
    f"3. City with the highest number of orders: "
    f"{top_city} ({top_city_orders} orders)"
)


# Gender with highest number of orders
top_gender = df["Gender"].value_counts().idxmax()
top_gender_orders = df["Gender"].value_counts().max()

print(
    f"4. Gender with the highest number of orders: "
    f"{top_gender} ({top_gender_orders} orders)"
)


# Average sales
average_sales = df["Total_Sales"].mean()

print(
    f"5. Average Total Sales per order: "
    f"{average_sales:,.2f}"
)


# Maximum sales
maximum_sales = df["Total_Sales"].max()

print(
    f"6. Highest Total Sales in a single order: "
    f"{maximum_sales:,.2f}"
)


# Average quantity
average_quantity = df["Quantity"].mean()

print(
    f"7. Average quantity per order: "
    f"{average_quantity:.2f}"
)


# Average customer age
average_age = df["Age"].mean()

print(
    f"8. Average customer age: "
    f"{average_age:.2f}"
)


# ============================================================
# 8. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("--- CORRELATION MATRIX ---")
print("=" * 60)

correlation_matrix = df[numerical_columns].corr()

print(correlation_matrix)


# ============================================================
# 9. STRONGEST CORRELATIONS
# ============================================================

print("\n" + "=" * 60)
print("--- CORRELATION WITH TOTAL SALES ---")
print("=" * 60)

sales_correlation = correlation_matrix["Total_Sales"].sort_values(
    ascending=False
)

print(sales_correlation)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 60)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)