# Assignment 50 - MySQL 2

/* Question 3: 

ALTER students Table
Task:

Add a column dob DATE

Rename column phone to mobile_number

Modify column age to SMALLINT

Drop column email

*/

-- Add dob column
ALTER TABLE students
ADD dob DATE;

-- Rename phone to mobile_number
ALTER TABLE students
RENAME COLUMN phone TO mobile_number;

-- Modify age to SMALLINT
ALTER TABLE students
MODIFY COLUMN age SMALLINT;

-- Drop email column
ALTER TABLE students
DROP COLUMN email;

-- Check the updated structure
DESC students;