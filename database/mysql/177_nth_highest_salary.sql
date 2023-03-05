CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET n = N - 1;
  RETURN (
      SELECT distinct(e.salary) 
      FROM employee as e
      ORDER BY e.salary DESC
      LIMIT 1
      OFFSET n
  );
END