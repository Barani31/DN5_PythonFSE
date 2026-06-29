CREATE TABLE Student(

id SERIAL PRIMARY KEY,

name VARCHAR(50),

age INT,

marks NUMERIC(5,2),

dob DATE,

created_at TIMESTAMP,

active BOOLEAN

);