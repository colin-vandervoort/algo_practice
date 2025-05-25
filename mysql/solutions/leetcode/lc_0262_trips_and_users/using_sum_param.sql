WITH
    unbanned_users AS (SELECT * FROM Users WHERE banned = 'No'),
    counted_trips AS (
        SELECT
            *
        FROM
            Trips
        WHERE
            client_id IN (SELECT users_id FROM unbanned_users)
            AND driver_id IN (SELECT users_id FROM unbanned_users)
    )
SELECT
    counted_trips.request_at AS Day,
    ROUND(
        SUM(counted_trips.status != 'completed') / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM
    counted_trips
WHERE
    counted_trips.request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
    Day;