CREATE TABLE Department(

dept_id INT PRIMARY KEY,

dept_name VARCHAR(50)

);

CREATE TABLE Student(

student_id INT PRIMARY KEY,

name VARCHAR(50),

dept_id INT,

FOREIGN KEY(dept_id)

REFERENCES Department(dept_id)

);

CREATE TABLE Course(

course_id INT PRIMARY KEY,

course_name VARCHAR(50),

dept_id INT,

FOREIGN KEY(dept_id)

REFERENCES Department(dept_id)

);