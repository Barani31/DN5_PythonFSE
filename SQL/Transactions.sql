START TRANSACTION;

UPDATE Account
SET balance=balance-1000
WHERE id=1;

UPDATE Account
SET balance=balance+1000
WHERE id=2;

COMMIT;