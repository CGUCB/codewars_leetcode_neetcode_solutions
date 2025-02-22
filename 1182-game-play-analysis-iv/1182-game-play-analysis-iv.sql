WITH CTE AS (
    SELECT
        player_id,
        DATE_ADD(MIN(event_date), INTERVAL 1 DAY) AS event_date
    FROM
        Activity
    GROUP BY
        player_id
)
SELECT
    ROUND(
        COUNT(a.player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction
FROM
    Activity AS a
INNER JOIN
    CTE AS c
ON
    a.player_id = c.player_id AND
    a.event_date = c.event_date