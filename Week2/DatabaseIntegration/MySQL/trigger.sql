
DELIMITER //

CREATE TRIGGER employee_insert

AFTER INSERT

ON Employee

FOR EACH ROW

BEGIN

INSERT INTO EmployeeLog(message)

VALUES(CONCAT(NEW.emp_name,' Added'));

END //

DELIMITER ;