-- Write your PostgreSQL query statement below
SELECT Employee.name as Employee FROM Employee 
    WHERE Employee.Salary > (SELECT salary FROM Employee AS E Where Id = Employee.ManagerId)