CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    # Write your MySQL query statement below.
    SELECT
        s.salary
    FROM (
        SELECT
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
        FROM
            Employee
    ) AS s
    WHERE
        s.rnk = N
    UNION
        SELECT
            NULL
    LIMIT 1
  );
END