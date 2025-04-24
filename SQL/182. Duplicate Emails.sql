-- Write your PostgreSQL query statement below
SELECT Person.email as Email from Person GROUP BY Person.email Having count(Email) > 1;