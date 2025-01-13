# Write your MySQL query statement below
SELECT DISTINCT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND
    recyclable = 'Y'