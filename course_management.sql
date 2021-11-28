-- Create the course_management database
CREATE DATABASE course_management;

-- Create the tables student, instructor, course, department, user.
CREATE TABLE students (
	id SERIAL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
	gpa INT NOT NULL,
    user_id INT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE instructors (
	id SERIAL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL,
	password TEXT NOT NULL,
    user_id INT NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE teaches (
    instructor_id INT,
    student_id INT,
    PRIMARY KEY(instructor_id, student_id)
);

CREATE TABLE departments (
	id SERIAL,
	name TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE employs (
	department_id INT,
	instructor_id INT,
	PRIMARY KEY (department_id, instructor_id)
);

CREATE TABLE courses (
	id SERIAL,
	name TEXT NOT NULL,
	max_capacity INT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE users (
	id SERIAL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE advises (
	instructor_id INT,
	student_id INT,
	PRIMARY KEY(instructor_id, student_id)
);

CREATE TABLE takes (
    course_id INT,
    student_id INT,
    PRIMARY KEY(course_id, student_id)
);

-- Create the alter table to link the email and password from the user table to the student and instructor table. 
ALTER TABLE students
ADD CONSTRAINT fk_students_users
FOREIGN KEY (user_id)
REFERENCES users;

ALTER TABLE instructors
ADD CONSTRAINT fk_instructors_users
FOREIGN KEY (user_id)
REFERENCES users;

-- Create the alter table to link the instructor to the course
ALTER TABLE teaches
ADD CONSTRAINT fk_teaches_instructors
FOREIGN KEY (instructor_id)
REFERENCES instructors;

ALTER TABLE teaches
ADD CONSTRAINT fk_teaches_student
FOREIGN KEY (student_id)
REFERENCES students;

-- Create the alter table to link the instructor to the department
ALTER TABLE employs
ADD CONSTRAINT fk_employs_departments
FOREIGN KEY (department_id)
REFERENCES departments;

ALTER TABLE employs
ADD CONSTRAINT fk_employs_instructors
FOREIGN KEY (instructor_id)
REFERENCES instructors;

-- Create the alter table to link the instructor who advises the student
ALTER TABLE advises
ADD CONSTRAINT fk_advises_instructors
FOREIGN KEY(instructor_id)
REFERENCES instructors;

ALTER TABLE advises
ADD CONSTRAINT fk_advises_students
FOREIGN KEY(student_id)
REFERENCES students;

-- Create the alter table to link the courses that a student takes
ALTER TABLE takes
ADD CONSTRAINT fk_takes_courses
FOREIGN KEY(course_id)
REFERENCES courses;

ALTER TABLE takes
ADD CONSTRAINT fk_takes_students
FOREIGN KEY (student_id)
REFERENCES students;