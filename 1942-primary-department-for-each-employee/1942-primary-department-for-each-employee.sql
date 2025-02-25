SELECT
    employee_id,
    department_id
FROM (
    SELECT
        employee_id,
        department_id,
        RANK() OVER (PARTITION BY employee_id ORDER BY primary_flag ASC) AS rnk
    FROM
        Employee
) AS e
WHERE
    rnk = 1