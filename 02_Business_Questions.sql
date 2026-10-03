
-- Q1 — Which city has the highest number of orders?
-- ============================================================
-- Q1. CITY-WISE ORDER COUNT
-- ============================================================

SELECT
    City,
    COUNT(Order_ID) AS Total_Orders
FROM sales
GROUP BY City
ORDER BY Total_Orders DESC;


-- Q2 — Which product has the highest total quantity sold?
-- ============================================================
-- Q2. PRODUCT-WISE TOTAL QUANTITY
-- ============================================================

SELECT
    Product,
    SUM(Quantity) AS Total_Quantity
FROM sales
GROUP BY Product
ORDER BY Total_Quantity DESC;



-- Q3 — Which category generates the highest total sales?
-- ============================================================
-- Q3. CATEGORY-WISE TOTAL SALES
-- ============================================================

SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- Q4 — What is the average sales per city?
-- ============================================================
-- Q4. CITY-WISE AVERAGE SALES
-- ============================================================

SELECT
    City,
    ROUND(AVG(Total_Sales), 2) AS Average_Sales
FROM sales
GROUP BY City
ORDER BY Average_Sales DESC;


-- Q5 — What are the total quantity and sales for each category?
-- ============================================================
-- Q5. CATEGORY-WISE QUANTITY AND SALES
-- ============================================================

SELECT
    Category,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;


-- Q6 — What is the average sales by gender?
-- ============================================================
-- Q6. GENDER-WISE AVERAGE SALES
-- INNER JOIN: sales + customers
-- ============================================================

SELECT
    c.Gender,
    COUNT(s.Order_ID) AS Total_Orders,
    ROUND(AVG(s.Total_Sales), 2) AS Average_Sales
FROM sales AS s
INNER JOIN customers AS c
    ON s.Customer_ID = c.Customer_ID
GROUP BY c.Gender
ORDER BY Average_Sales DESC;


-- Q7 — High-value orders: Product-wise sales
-- ============================================================
-- Q7. HIGH-VALUE ORDERS BY PRODUCT
-- Orders above 100,000
-- INNER JOIN: sales + products
-- ============================================================

SELECT
    p.Product,
    p.Category,
    SUM(s.Quantity) AS Total_Quantity,
    ROUND(SUM(s.Total_Sales), 2) AS Total_Sales
FROM sales AS s
INNER JOIN products AS p
    ON s.Product = p.Product
WHERE s.Total_Sales > 100000
GROUP BY
    p.Product,
    p.Category
ORDER BY Total_Sales DESC;


