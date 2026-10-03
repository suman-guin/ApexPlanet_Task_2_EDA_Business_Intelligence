import pandas as pd
import matplotlib.pyplot as plt
import os

# Project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Dataset path
dataset_path = os.path.join(
    BASE_DIR,
    "01_Dataset",
    "ApexPlanet_Cleaned_Dataset.xlsx"
)

# Visualization output folder
output_dir = os.path.join(
    BASE_DIR,
    "04_Visualizations"
)

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_excel(dataset_path)


# # --------------------------------
# # 1. Gender Distribution
# # --------------------------------

# # 1. Gender Distribution

# gender_counts = df["Gender"].value_counts()

# plt.figure(figsize=(8, 5))
# gender_counts.plot(kind="bar")

# plt.title("Gender Distribution")
# plt.xlabel("Gender")
# plt.ylabel("Number of Orders")
# plt.xticks(rotation=0)

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "01_Gender_Distribution.png"),
#     dpi=300
# )

# plt.show()


# # --------------------------------
# # 2. City Distribution
# # --------------------------------

# city_counts = df["City"].value_counts()

# plt.figure(figsize=(9, 5))
# city_counts.plot(kind="bar")

# plt.title("Orders by City")
# plt.xlabel("City")
# plt.ylabel("Number of Orders")
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.savefig("../04_Visualizations/02_City_Distribution.png", dpi=300)
# plt.show()


# # --------------------------------
# # 3. Product Distribution
# # --------------------------------

# product_counts = df["Product"].value_counts()

# plt.figure(figsize=(8, 5))
# product_counts.plot(kind="bar")

# plt.title("Product Distribution")
# plt.xlabel("Product")
# plt.ylabel("Number of Orders")
# plt.xticks(rotation=0)

# plt.tight_layout()
# plt.savefig("../04_Visualizations/03_Product_Distribution.png", dpi=300)
# plt.show()


# # --------------------------------
# # 4. Category Distribution
# # --------------------------------

# category_counts = df["Category"].value_counts()

# plt.figure(figsize=(8, 5))
# category_counts.plot(kind="bar")

# plt.title("Category Distribution")
# plt.xlabel("Category")
# plt.ylabel("Number of Orders")
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.savefig("../04_Visualizations/04_Category_Distribution.png", dpi=300)
# plt.show()




# # ============================================================
# # NUMERICAL ANALYSIS - HISTOGRAMS
# # ============================================================

# # 5. Age Distribution

# plt.figure(figsize=(8, 5))

# plt.hist(df["Age"], bins=10, edgecolor="black")

# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "05_Age_Distribution.png"),
#     dpi=300
# )

# plt.show()


# # ============================================================
# # 6. Quantity Distribution
# # ============================================================

# plt.figure(figsize=(8, 5))

# plt.hist(df["Quantity"], bins=10, edgecolor="black")

# plt.title("Quantity Distribution")
# plt.xlabel("Quantity")
# plt.ylabel("Frequency")

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "06_Quantity_Distribution.png"),
#     dpi=300
# )

# plt.show()


# # ============================================================
# # 7. Unit Price Distribution
# # ============================================================

# plt.figure(figsize=(8, 5))

# plt.hist(df["Unit_Price"], bins=10, edgecolor="black")

# plt.title("Unit Price Distribution")
# plt.xlabel("Unit Price")
# plt.ylabel("Frequency")

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "07_Unit_Price_Distribution.png"),
#     dpi=300
# )

# plt.show()


# ============================================================
# 8. Total Sales Distribution
# ============================================================

# plt.figure(figsize=(8, 5))

# plt.hist(df["Total_Sales"], bins=10, edgecolor="black")

# plt.title("Total Sales Distribution")
# plt.xlabel("Total Sales")
# plt.ylabel("Frequency")

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "08_Total_Sales_Distribution.png"),
#     dpi=300
# )

# plt.show()

# # ============================================================
# # 5. Age Distribution
# # ============================================================

# plt.figure(figsize=(8, 5))

# plt.hist(df["Age"], bins=10, edgecolor="black")

# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")

# plt.tight_layout()

# plt.savefig(
#     os.path.join(output_dir, "05_Age_Distribution.png"),
#     dpi=300
# )

# plt.show()



# ============================================================
# MULTIVARIATE ANALYSIS & CORRELATION
# ============================================================

# Numerical columns
numerical_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]


# ============================================================
# 9. Correlation Heatmap
# ============================================================

correlation_matrix = df[numerical_columns].corr()

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    interpolation="nearest"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(numerical_columns)),
    numerical_columns,
    rotation=45
)

plt.yticks(
    range(len(numerical_columns)),
    numerical_columns
)

plt.title("Correlation Heatmap")

# Display correlation values
for i in range(len(numerical_columns)):
    for j in range(len(numerical_columns)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "09_Correlation_Heatmap.png"),
    dpi=300
)

plt.show()


# ============================================================
# 10. Quantity vs Total Sales
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Quantity"],
    df["Total_Sales"],
    alpha=0.6
)

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "10_Quantity_vs_Total_Sales.png"),
    dpi=300
)

plt.show()


# ============================================================
# 11. Unit Price vs Total Sales
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Unit_Price"],
    df["Total_Sales"],
    alpha=0.6
)

plt.title("Unit Price vs Total Sales")
plt.xlabel("Unit Price")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "11_Unit_Price_vs_Total_Sales.png"),
    dpi=300
)

plt.show()


# ============================================================
# 12. Age vs Total Sales
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Age"],
    df["Total_Sales"],
    alpha=0.6
)

plt.title("Age vs Total Sales")
plt.xlabel("Age")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "12_Age_vs_Total_Sales.png"),
    dpi=300
)

plt.show()


# ============================================================
# MULTIVARIATE ANALYSIS COMPLETED
# ============================================================

print("\nMultivariate Analysis Visualizations Generated Successfully!")