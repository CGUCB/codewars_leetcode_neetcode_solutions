# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        *,
        RANK() OVER (ORDER BY recordDate ASC) AS rnk
    FROM
        Weather
)
SELECT
    w1.id
FROM
    CTE AS w1
JOIN
    CTE AS w2
ON
    w1.rnk = (w2.rnk + 1)
WHERE
    w2.temperature IS NOT NULL AND
    w1.temperature > w2.temperature AND
    DATEDIFF(w1.recordDate, w2.recordDate) = 1