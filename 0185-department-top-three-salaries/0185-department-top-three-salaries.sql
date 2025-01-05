# Write your MySQL query statement below
SELECT
    t.Department,
    t.Employee,
    t.Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentID 
            ORDER BY e.salary DESC
            ) AS rnk
    FROM
        Employee AS e
    INNER JOIN
        Department AS d
    ON
        e.departmentId = d.id
    ) AS t
WHERE
    rnk <= 3