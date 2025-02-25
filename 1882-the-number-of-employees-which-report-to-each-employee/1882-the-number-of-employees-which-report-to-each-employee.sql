SELECT
    e.reports_to AS employee_id,
    e1.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e.age), 0) AS average_age
FROM
    Employees AS e
JOIN (
    SELECT
        employee_id,
        name
    FROM
        Employees
    ) AS e1
ON
    e.reports_to = e1.employee_id
WHERE
    e.reports_to IS NOT NULL
GROUP BY
    e.reports_to
ORDER BY
    employee_id