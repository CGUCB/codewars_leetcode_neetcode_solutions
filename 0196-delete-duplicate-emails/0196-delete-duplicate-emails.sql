DELETE FROM 
    Person
WHERE
    id IN (
        SELECT
            id
        FROM (
            SELECT
                *,
                RANK() OVER (PARTITION BY email ORDER BY id ASC) AS rnk
            FROM
                Person
        ) AS p
        WHERE
            rnk > 1
    )
