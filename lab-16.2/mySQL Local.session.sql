-- Drop the database if it already exists (optional but useful)
DROP DATABASE IF EXISTS company_db;

-- Create a new database
CREATE DATABASE company_db;

-- Switch to that database
USE company_db;

-- Create the department table first (because employee references it)
CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(100)
);

-- Now create the employee table with a foreign key referencing department
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department INT,
    salary DECIMAL(10, 2),
    hire_date DATE,
    FOREIGN KEY (department) REFERENCES department(dept_id)
);

-- Insert values into the department table
INSERT INTO department (dept_id, dept_name, location) VALUES
(1, 'Human Resources', 'New York'),
(2, 'Engineering', 'San Francisco'),
(3, 'Sales', 'Chicago');

-- Insert values into the employee table
INSERT INTO employee (emp_id, first_name, last_name, department, salary, hire_date) VALUES
(1, 'John', 'Doe', 2, 75000.00, '2022-01-15'),
(2, 'Jane', 'Smith', 1, 60000.00, '2021-03-22'),
(3, 'Emily', 'Johnson', 3, 50000.00, '2023-05-10');

-- Display all records from both tables
SELECT * FROM department;
SELECT * FROM employee;

SELECT 
    e.first_name,
    e.last_name,
    d.dept_name
FROM employee e
JOIN department d
    ON e.department = d.dept_id;

SELECT DISTINCT dept_name
FROM department;

SELECT *
FROM employee
WHERE salary > 50000;

SELECT e.*
FROM employee e
JOIN department d
    ON e.department = d.dept_id
WHERE d.dept_name = 'IT';

SELECT *
FROM employee
WHERE hire_date > '2020-12-31';

SELECT *
FROM employee
ORDER BY salary ASC;

SELECT AVG(salary) AS avg_salary
FROM employee;

SELECT 
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employee;


SELECT 
    d.dept_name,
    SUM(e.salary) AS total_salary
FROM employee e
JOIN department d
    ON e.department = d.dept_id
GROUP BY d.dept_name;

SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS num_employees
FROM department d
JOIN employee e
    ON d.dept_id = e.department
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 1;
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS employee_count
FROM department d
LEFT JOIN employee e
    ON d.dept_id = e.department
GROUP BY d.dept_name;

SELECT 
    d.dept_name,
    AVG(e.salary) AS avg_salary
FROM department d
JOIN employee e
    ON d.dept_id = e.department
GROUP BY d.dept_name;

SELECT *
FROM employee
WHERE salary BETWEEN 45000 AND 60000;

SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name
FROM employee;

SELECT 
    UPPER(first_name) AS first_name_upper,
    UPPER(last_name)  AS last_name_upper
FROM employee;


SELECT
    emp_id,
    first_name,
    last_name,
    DATEDIFF(CURDATE(), hire_date) AS days_since_hired
FROM employee;
SELECT *
FROM employee
WHERE YEAR(hire_date) = 2020;

SELECT *
FROM employee
WHERE last_name LIKE '%a';

SELECT *
FROM employee
WHERE first_name LIKE 'A%';

SELECT 
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary
FROM employee;

SELECT 
    d.location AS city,
    COUNT(e.emp_id) AS employee_count
FROM department d
LEFT JOIN employee e
       ON e.department = d.dept_id
GROUP BY d.location;

SELECT 
    d.dept_name,
    AVG(e.salary) AS avg_salary
FROM department d
JOIN employee e
      ON d.dept_id = e.department
GROUP BY d.dept_name
ORDER BY avg_salary DESC
LIMIT 2;

SELECT *
FROM employee
WHERE salary > ( SELECT AVG(salary) FROM employee );

SELECT 
    d.dept_name,
    AVG(e.salary) AS avg_salary
FROM employee e
JOIN department d
    ON e.department = d.dept_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC
LIMIT 1;


SELECT *
FROM employee
ORDER BY hire_date DESC;

SELECT *
FROM employee
WHERE salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE salary < (SELECT MAX(salary) FROM employee)
);

SELECT *
FROM employee
WHERE department = (
        SELECT department
        FROM employee
        WHERE first_name = 'Amit'
          AND last_name  = 'Sharma'
);

UPDATE employee
SET salary = salary * 1.10
WHERE department = (
    SELECT dept_id
    FROM department
    WHERE dept_name = 'IT'
);

UPDATE employee
SET salary = salary * 1.10
WHERE department = (
    SELECT dept_id FROM department WHERE dept_name = 'Engineering'
);
SELECT 
    YEAR(hire_date) AS hire_year,
    COUNT(*) AS employee_count
FROM employee
GROUP BY YEAR(hire_date);

SELECT 
    e.emp_id,
    e.first_name,
    e.last_name,
    d.location AS department_location
FROM employee e
JOIN department d
    ON e.department = d.dept_id;


SELECT e.*
FROM employee e
JOIN department d
    ON e.department = d.dept_id
WHERE d.location = 'Bangalore';

SELECT 
    e.*,
    d.dept_name
FROM employee e
LEFT JOIN department d
       ON e.department = d.dept_id;


SELECT d.dept_name
FROM department d
LEFT JOIN employee e
       ON d.dept_id = e.department
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) = 0;

CREATE VIEW high_salary_employees AS
SELECT *
FROM employee
WHERE salary > 55000;

ALTER TABLE department
MODIFY dept_name VARCHAR(50) NOT NULL;

RENAME TABLE employee TO staff;


CREATE TABLE employee_backup AS
SELECT * FROM employee;

TRUNCATE TABLE employee;

DROP TABLE employee_backup;

CREATE INDEX idx_last_name
ON employee(last_name);


DROP INDEX idx_last_name
ON employee;