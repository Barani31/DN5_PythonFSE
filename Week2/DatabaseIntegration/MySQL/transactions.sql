START TRANSACTION;

UPDATE Employee

SET salary=salary+5000

WHERE emp_id=1;

UPDATE Employee

SET salary=salary-5000

WHERE emp_id=2;

COMMIT;