# Write your MySQL query statement below
SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rnk
    FROM
        Employee AS e
    LEFT JOIN
        Department AS d
    ON
        e.departmentId = d.id
) AS t
WHERE
    rnk = 1