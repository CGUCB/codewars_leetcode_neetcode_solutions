SELECT
    visited_on,
    SUM(amt) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND(AVG(amt) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
FROM (
    SELECT
        visited_on,
        SUM(amount) AS amt
    FROM
        Customer
    GROUP BY
        visited_on
    ) AS c
ORDER BY
    visited_on ASC
LIMIT 1000000
OFFSET 6