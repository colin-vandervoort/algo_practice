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
    ),
    daily_trip_counts AS (
        SELECT
            count(*) AS qty,
            request_at
        FROM
            counted_trips
        GROUP BY request_at
        WINDOW w AS (PARTITION BY request_at)
    ),
    daily_cancelled_trip_counts AS (
        SELECT
            count(*) AS qty,
            request_at
        FROM
            counted_trips
        WHERE
            status IN ('cancelled_by_driver', 'cancelled_by_client')
        GROUP BY request_at
        WINDOW w AS (PARTITION BY request_at)
    )
SELECT
    daily_trip_counts.request_at AS Day,
    ROUND(COALESCE(daily_cancelled_trip_counts.qty, 0) / daily_trip_counts.qty, 2) AS 'Cancellation Rate'
FROM
    daily_trip_counts
LEFT JOIN
    daily_cancelled_trip_counts
ON
    daily_cancelled_trip_counts.request_at = daily_trip_counts.request_at
WHERE
    daily_trip_counts.request_at BETWEEN "2013-10-01" AND "2013-10-03"