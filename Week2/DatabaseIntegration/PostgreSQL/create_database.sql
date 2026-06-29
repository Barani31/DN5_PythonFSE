CREATE DATABASE companydb;

\c companydb

CREATE TABLE Employee(

emp_id SERIAL PRIMARY KEY,

emp_name VARCHAR(100),

department VARCHAR(50),

salary NUMERIC(10,2)

);

INSERT INTO Employee(emp_name,department,salary)

VALUES

('Barani','IT',50000),

('Arun','HR',40000),

('John','IT',65000),

('David','Sales',45000);