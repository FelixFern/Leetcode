-- Write your PostgreSQL query statement below
SELECT (SELECT DISTINCT salary From Employee
ORDER BY salary DESC 
LIMIT 1 OFFSET 1) AS SecondHighestSalary
