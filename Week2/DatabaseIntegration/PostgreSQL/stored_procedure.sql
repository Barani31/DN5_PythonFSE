CREATE OR REPLACE FUNCTION

EmployeeCount()

RETURNS INTEGER

LANGUAGE plpgsql

AS

$$

DECLARE

total INTEGER;

BEGIN

SELECT COUNT(*)

INTO total

FROM Employee;

RETURN total;

END;

$$;


CREATE OR REPLACE PROCEDURE

IncreaseSalary()

LANGUAGE plpgsql

AS

$$

BEGIN

UPDATE Employee

SET salary=salary+5000;

END;

$$;