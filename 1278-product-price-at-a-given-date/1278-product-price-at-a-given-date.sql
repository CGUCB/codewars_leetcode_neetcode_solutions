WITH CTE AS (
    SELECT
        product_id,
        new_price,
        change_date,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)
SELECT DISTINCT
    p1.product_id,
    COALESCE(p2.new_price, 10) AS price
FROM
    Products AS p1
LEFT JOIN (
    SELECT * FROM CTE WHERE rnk = 1
    ) AS p2
ON
    p1.product_id = p2.product_id
