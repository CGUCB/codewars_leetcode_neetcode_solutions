WITH CTE AS (
    SELECT
        q.person_id,
        q.person_name,
        q.weight,
        q.turn,
        (SELECT SUM(q2.weight)
        FROM Queue AS q2
        WHERE q2.turn <= q.turn) AS cumsum
    FROM
        Queue AS q
    ORDER BY
        q.turn ASC
)
SELECT 
    person_name
FROM 
    CTE
WHERE 
    turn IN (SELECT MAX(turn) FROM CTE WHERE cumsum <= 1000)
