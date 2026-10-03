-- ============================================================
-- APEXPLANET TASK 2
-- DATABASE SETUP
-- ============================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS apexplanet_task2;

USE apexplanet_task2;


-- ============================================================
-- 1. SALES TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS sales (
    Order_ID VARCHAR(50),
    Order_Date DATE,
    Customer_ID VARCHAR(50),
    Customer_Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(20),
    City VARCHAR(50),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Total_Sales DECIMAL(15,2)
);


-- ============================================================
-- 2. CUSTOMERS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS customers (
    Customer_ID VARCHAR(50) PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(20),
    City VARCHAR(50)
);


-- ============================================================
-- 3. PRODUCTS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS products (
    Product VARCHAR(50) PRIMARY KEY,
    Category VARCHAR(50)
);



-- ============================================================
-- POPULATE CUSTOMERS TABLE
-- ============================================================

INSERT IGNORE INTO customers
    (Customer_ID, Customer_Name, Age, Gender, City)
SELECT DISTINCT
    Customer_ID,
    Customer_Name,
    Age,
    Gender,
    City
FROM sales;


-- ============================================================
-- POPULATE PRODUCTS TABLE
-- ============================================================

INSERT IGNORE INTO products
    (Product, Category)
SELECT DISTINCT
    Product,
    Category
FROM sales;


-- ============================================================
-- VERIFICATION
-- ============================================================

SELECT COUNT(*) AS Sales_Count
FROM sales;

SELECT COUNT(*) AS Customer_Count
FROM customers;

SELECT COUNT(*) AS Product_Count
FROM products;

SELECT *
FROM products;

SELECT *
FROM customers
LIMIT 10;