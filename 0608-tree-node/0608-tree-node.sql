# Write your MySQL query statement below
SELECT
    id,
    'Root' AS type
FROM
    Tree AS t
WHERE
    t.p_id IS NULL
UNION
SELECT
    id,
    'Inner' AS type
FROM
    Tree AS t
WHERE 
    EXISTS (
        SELECT 
            1 
        FROM 
            Tree AS s
        WHERE
            t.id = s.p_id
        ) AND
    p_id IS NOT NULL
UNION
SELECT
    id,
    'Leaf' AS type
FROM
    Tree AS t
WHERE 
    NOT EXISTS (
        SELECT 
            1 
        FROM 
            Tree AS s
        WHERE
            t.id = s.p_id
        ) AND
    p_id IS NOT NULL