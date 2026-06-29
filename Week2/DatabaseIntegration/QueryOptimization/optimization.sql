SELECT *

FROM Employee

WHERE department='IT';

CREATE INDEX idx_dept

ON Employee(department);

SELECT *

FROM Employee

WHERE department='IT';