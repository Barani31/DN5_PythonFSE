# Database Normalization

## First Normal Form (1NF)
- Atomic values
- No repeating groups

Example

StudentID | Name | Subject
1         | Barani | Python

---

## Second Normal Form (2NF)
- Must satisfy 1NF
- Remove partial dependency

---

## Third Normal Form (3NF)
- Must satisfy 2NF
- Remove transitive dependency

Example

Student
---------
StudentID
StudentName
DepartmentID

Department
-----------
DepartmentID
DepartmentName