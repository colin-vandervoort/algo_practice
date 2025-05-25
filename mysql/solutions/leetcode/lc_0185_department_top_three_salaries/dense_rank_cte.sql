WITH
    intra_dept_ranks (dept_id, employee_name, salary, salary_rank) AS (
        SELECT
            departmentId,
            name,
            salary,
            dense_rank() OVER w AS salary_rank
        FROM
            Employee
        WINDOW w AS (PARTITION BY departmentId ORDER BY salary DESC)
    )
SELECT
    Department.name AS Department,
    intra_dept_ranks.employee_name AS Employee,
    intra_dept_ranks.salary AS Salary
FROM
    intra_dept_ranks
INNER JOIN
    Department
ON
    Department.id = intra_dept_ranks.dept_id
WHERE
    salary_rank < 4;