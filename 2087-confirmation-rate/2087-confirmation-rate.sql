# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        s.user_id AS user_id,
        (CASE
            WHEN c.action = 'confirmed' THEN 1
            WHEN c.action = 'timeout' THEN 0
            ELSE 0
        END) AS confirmation_ind
    FROM
        Signups AS s
    LEFT JOIN
        Confirmations AS c
    ON
        s.user_id = c.user_id
)
SELECT
    user_id,
    ROUND(AVG(confirmation_ind), 2) AS confirmation_rate
FROM
    CTE
GROUP BY
    user_id
ORDER BY
    confirmation_rate ASC