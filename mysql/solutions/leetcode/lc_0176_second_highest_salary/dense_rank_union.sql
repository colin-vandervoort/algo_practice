WITH
    ranking_cte (salary, salary_rank) AS (
        SELECT
            salary,
            dense_rank() OVER w
        FROM
            Employee
        WINDOW w AS (ORDER BY salary DESC)
    ),
    target_data (salary) AS (
        SELECT salary FROM ranking_cte WHERE salary_rank = 2
    )
SELECT
    target_data.salary AS SecondHighestSalary
FROM
    target_data
UNION
    SELECT NULL AS SecondHighestSalary
WHERE
    NOT EXISTS (SELECT * FROM target_data)
LIMIT 1;