WITH
    ranking_cte (salary, salary_rank) AS (
        SELECT
            salary,
            dense_rank() OVER w
        FROM
            Employee
        WINDOW w AS (ORDER BY salary DESC)
    ),
    target_rank_cte (target_rank) AS (SELECT 2 AS target_rank)
SELECT
    ranking_cte.salary
FROM
    target_rank_cte
LEFT JOIN
    ranking_cte
ON
    ranking_cte.salary_rank = target_rank_cte.target_rank;