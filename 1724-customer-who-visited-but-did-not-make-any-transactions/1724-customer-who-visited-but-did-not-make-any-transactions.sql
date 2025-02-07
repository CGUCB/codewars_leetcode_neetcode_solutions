SELECT
    v.customer_id AS customer_id,
    SUM(
        CASE
            WHEN t.transaction_id IS NULL THEN 1
            ELSE 0
        END
    ) AS count_no_trans
FROM
    Visits AS v
LEFT JOIN
    Transactions AS t
ON
    v.visit_id = t.visit_id
GROUP BY
    v.customer_id
HAVING
    count_no_trans > 0