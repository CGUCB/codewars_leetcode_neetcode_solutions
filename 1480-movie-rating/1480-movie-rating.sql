(SELECT
    u.name AS results
FROM
    MovieRating AS mr
LEFT JOIN
    Users AS u
ON
    u.user_id = mr.user_id
GROUP BY
    u.user_id
ORDER BY
    COUNT(*) DESC,
    u.name ASC
LIMIT 1)
UNION ALL
(SELECT
    m.title AS results
FROM
    MovieRating AS mr
JOIN
    Movies AS m
ON
    m.movie_id = mr.movie_id
WHERE
    DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
GROUP BY
    m.title
ORDER BY
    AVG(mr.rating) DESC,
    m.title ASC
LIMIT 1)