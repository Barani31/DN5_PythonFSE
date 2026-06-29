SELECT AVG(salary)

FROM Employee;

SELECT MAX(salary)

FROM Employee;

SELECT department,

COUNT(*)

FROM Employee

GROUP BY department;

SELECT department,

AVG(salary)

FROM Employee

GROUP BY department

HAVING AVG(salary)>45000;

SELECT

emp_name,

salary,

RANK()

OVER(ORDER BY salary DESC)

FROM Employee;

WITH HighSalary AS(

SELECT *

FROM Employee

WHERE salary>45000

)

SELECT *

FROM HighSalary;

