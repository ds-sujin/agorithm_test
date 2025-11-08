-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Sales a JOIN Product b on a.product_id = b.product_id
