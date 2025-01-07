# Write your MySQL query statement below
SELECT
    salary AS SecondHighestSalary
FROM (
    SELECT DISTINCT
        id,
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS r
    FROM
        Employee
) AS t
WHERE
    r = 2
UNION
    SELECT
        Null
LIMIT 1