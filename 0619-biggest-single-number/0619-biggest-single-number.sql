((SELECT
    num
FROM
    MyNumbers
GROUP BY
    num
HAVING
    COUNT(*) = 1)
UNION ALL
(SELECT NULL))
ORDER BY
    num DESC
LIMIT 1