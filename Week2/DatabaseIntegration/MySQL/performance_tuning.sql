CREATE INDEX idx_department

ON Employee(department);

EXPLAIN

SELECT *

FROM Employee

WHERE department='IT';

EXPLAIN ANALYZE

SELECT *

FROM Employee

WHERE department='IT';