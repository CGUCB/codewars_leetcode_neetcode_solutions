WITH CTE AS (
    SELECT
        person_name,
        turn,
        SUM(weight) OVER(ORDER BY turn) AS cumsum
    FROM
        Queue
    ORDER BY
        turn ASC
)
SELECT 
    person_name
FROM 
    CTE
WHERE 
    turn IN (SELECT MAX(turn) FROM CTE WHERE cumsum <= 1000)
