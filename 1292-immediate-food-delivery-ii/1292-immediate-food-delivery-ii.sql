SELECT
    ROUND(
        100 * AVG(
            CASE WHEN order_date = customer_pref_delivery_date THEN 1
            ELSE 0
            END
        ), 2
    ) AS immediate_percentage
FROM (
    SELECT
        order_date,
        customer_pref_delivery_date,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rnk
    FROM
        Delivery
    ) AS d
WHERE
    rnk = 1