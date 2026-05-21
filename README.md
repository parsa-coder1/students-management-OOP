# Student Management System OOP

An upgraded Student Management System built with Python using Object-Oriented Programming (OOP).

This project manages students, courses, enrollments, and data persistence using JSON files.

---

# Features

- Add students
- Show all students
- Search students by ID or name
- Delete students
- Add courses
- Show all courses
- Search courses by ID or name
- Delete courses
- Enroll students in courses
- Unenroll students from courses
- Save data to JSON
- Load data automatically from JSON
- Bidirectional relationship between students and courses
- Modular project structure

---

# Concepts Used

This project practices:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Special Methods (`__str__`)
- Methods
- Lists and Loops
- Helper Functions
- Input Validation
- Object Relationships
- JSON File Handling
- Data Persistence
- Modular Programming

---

# Technologies

- Python 3

---

# File Structure

```text
student_management_system/
│
├── main.py
├── models.py
├── helpers.py
├── students_data.json
└── README.md
# Main Classes
Student
Represents a student and manages enrolled courses.
Course
Represents a course and manages enrolled students.
SystemManagement
Main system controller responsible for managing students, courses, enrollments, saving/loading data, and application operations.
 
# Run the Project
Bash
python main.py
 
# Author
Nasrullah Parsa