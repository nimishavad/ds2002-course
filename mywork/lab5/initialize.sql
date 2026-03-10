USE ced5jz_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    major VARCHAR(50),
    year INT
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    student_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO students VALUES (1,'Alex','CS',1);
INSERT INTO students VALUES (2,'Bella','Economics',2);
INSERT INTO students VALUES (3,'Chris','Math',3);
INSERT INTO students VALUES (4,'Dana','Biology',1);
INSERT INTO students VALUES (5,'Evan','Physics',2);
INSERT INTO students VALUES (6,'Faith','Chemistry',3);
INSERT INTO students VALUES (7,'George','History',4);
INSERT INTO students VALUES (8,'Hannah','CS',2);
INSERT INTO students VALUES (9,'Ian','Engineering',3);
INSERT INTO students VALUES (10,'Julia','Psychology',1);

INSERT INTO courses VALUES (101,'Data Science',1,'A');
INSERT INTO courses VALUES (102,'Statistics',2,'B');
INSERT INTO courses VALUES (103,'Calculus',3,'A');
INSERT INTO courses VALUES (104,'Biology',4,'B');
INSERT INTO courses VALUES (105,'Physics',5,'A');
INSERT INTO courses VALUES (106,'Chemistry',6,'B');
INSERT INTO courses VALUES (107,'World History',7,'A');
INSERT INTO courses VALUES (108,'Programming',8,'A');
INSERT INTO courses VALUES (109,'Engineering Design',9,'B');
INSERT INTO courses VALUES (110,'Psychology',10,'A');
