USE ced5jz_db;

SELECT students.name,
       students.major,
       courses.course_name,
       courses.grade
FROM students
JOIN courses
ON students.student_id = courses.student_id
WHERE courses.grade = 'A';