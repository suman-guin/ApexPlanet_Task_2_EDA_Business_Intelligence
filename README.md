# ApexPlanet Task 2 — EDA & Business Intelligence

## 📊 ApexPlanet Data Analytics Internship

This repository contains my **Task 2: Exploratory Data Analysis (EDA) & Business Intelligence** project completed as part of the **ApexPlanet Data Analytics Internship**.

The project focuses on analyzing a cleaned sales dataset using **Python, Pandas, SQL, Data Visualization, Correlation Analysis, and Business Intelligence techniques** to identify meaningful business insights.

---

## 🎯 Project Objective

The main objectives of this project are:

- Perform Exploratory Data Analysis on the cleaned sales dataset.
- Generate descriptive statistics and analyze data distributions.
- Identify important business patterns and trends.
- Use SQL to answer business-oriented questions.
- Perform multivariate and correlation analysis.
- Create meaningful data visualizations.
- Develop a static Business Intelligence dashboard.
- Present the final findings in a professional and understandable format.

---

## 📁 Dataset Overview

The cleaned dataset contains:

- **1,000 records**
- **12 columns**
- Customer information
- Order information
- Product information
- Sales and quantity information

### Main Columns

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of the order |
| Customer_ID | Customer identifier |
| Customer_Name | Customer name |
| Age | Customer age |
| Gender | Customer gender |
| City | Customer city |
| Product | Product name |
| Category | Product category |
| Quantity | Quantity ordered |
| Unit_Price | Price per unit |
| Total_Sales | Total sales value |

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **Matplotlib**
- **MySQL**
- **SQL**
- **Microsoft Excel**
- **Data Visualization**
- **Exploratory Data Analysis**
- **Business Intelligence**
- **PowerPoint**

---

## 🐍 Python EDA

Python and Pandas were used to perform:

- Dataset overview
- Data type analysis
- Descriptive statistics
- Numerical analysis
- Categorical analysis
- Distribution analysis
- Business insight extraction
- Correlation analysis

### Numerical Variables

The analysis covered:

- Age
- Quantity
- Unit Price
- Total Sales

### Categorical Variables

The analysis covered:

- Gender
- City
- Product
- Category

---

## 📈 Key EDA Insights

Some important findings from the analysis include:

- **Most frequently ordered product:** Mobile — 184 orders
- **Most frequently ordered category:** Electronics — 354 orders
- **City with the highest number of orders:** Patna — 135 orders
- **Gender with the highest number of orders:** Male — 511 orders
- **Average Total Sales per order:** ₹139,399.44
- **Highest single-order Total Sales:** ₹493,677.50
- **Average Quantity per order:** approximately 5.43
- **Average customer age:** approximately 41.34 years

---

## 🗄️ SQL Business Analysis

MySQL was used to answer business-oriented questions from the sales database.

The SQL analysis covered:

1. City-wise order count
2. Product-wise total quantity
3. Category-wise total sales
4. City-wise average sales
5. Category-wise quantity and sales performance
6. Gender-wise order and average sales analysis
7. High-value orders with Total Sales above ₹100,000

### Database Structure

The project uses three main tables:

- `sales`
- `customers`
- `products`

The final database contains:

- **1,000 sales records**
- **947 unique customers**
- **6 products**

---

## 🔗 Correlation & Multivariate Analysis

Correlation analysis was performed using:

- Age
- Quantity
- Unit Price
- Total Sales

### Important Correlations

| Variables | Correlation |
|---|---:|
| Quantity vs Total Sales | 0.6466 |
| Unit Price vs Total Sales | 0.6863 |
| Age vs Total Sales | 0.0008 |
| Quantity vs Unit Price | 0.0219 |

The analysis shows positive relationships between **Quantity and Total Sales** and between **Unit Price and Total Sales**, while Age has almost no linear relationship with Total Sales.

> Correlation indicates association between variables and does not establish causation.

---

## 📊 Data Visualizations

The project contains visualizations for:

1. Gender Distribution
2. City Distribution
3. Product Distribution
4. Category Distribution
5. Age Distribution
6. Quantity Distribution
7. Unit Price Distribution
8. Total Sales Distribution
9. Correlation Heatmap
10. Quantity vs Total Sales
11. Unit Price vs Total Sales
12. Age vs Total Sales

---

## 📌 Business Intelligence Dashboard

A static Business Intelligence dashboard was created to provide a quick overview of the sales dataset.

### Dashboard KPIs

- Total Sales
- Total Orders
- Average Sales per Order
- Average Quantity per Order

### Dashboard Analysis

The dashboard includes:

- Category-wise Sales
- City-wise Order Distribution
- Product-wise Order Distribution
- Correlation Analysis
- Key Business Insights

The dashboard provides a consolidated view of the major business metrics and analytical findings.

---

## 📂 Project Structure

```text
ApexPlanet_Task_2_EDA_Business_Intelligence/
│
├── 01_Dataset/
│   └── ApexPlanet_Cleaned_Dataset.xlsx
│
├── 02_Python_EDA/
│   ├── Task_2_EDA.py
│   └── visualizations.py
│
├── 03_SQL_Analysis/
│   ├── 01_Database_Setup.sql
│   ├── 02_Business_Questions.sql
│   └── 03_SQL_Results.txt
│
├── 04_Visualizations/
│   ├── 01_Gender_Distribution.png
│   ├── 02_City_Distribution.png
│   ├── 03_Product_Distribution.png
│   ├── 04_Category_Distribution.png
│   ├── 05_Age_Distribution.png
│   ├── 06_Quantity_Distribution.png
│   ├── 07_Unit_Price_Distribution.png
│   ├── 08_Total_Sales_Distribution.png
│   ├── 09_Correlation_Heatmap.png
│   ├── 10_Quantity_vs_Total_Sales.png
│   ├── 11_Unit_Price_vs_Total_Sales.png
│   └── 12_Age_vs_Total_Sales.png
│
├── 05_Dashboard/
│   └── ApexPlanet_Task2_Sales_Dashboard.png
│
├── 06_EDA_Report/
│   └── ApexPlanet_Task2_EDA_Report.pdf
│
└── README.md
