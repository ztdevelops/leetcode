SELECT max(salary) as SecondHighestSalary
FROM Employee
WHERE salary < (SELECT max(Salary) FROM Employee);