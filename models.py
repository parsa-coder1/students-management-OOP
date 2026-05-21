import json

import helpers


class Student:

    def __init__(self, student_id, name, student_class):
        self.id = student_id
        self.name = name
        self.student_class = student_class
        self.courses = []


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "student_class": self.student_class,
            "courses": [
                course.id for course in self.courses
            ]
        }
    

    def show_courses(self):
        if not self.courses:
            print("no course yet!")
            return
        
        for course in self.courses:
            print(course)
    

    def __str__(self):
        return f"{self.id} | {self.name} | {self.student_class}"


class Course:
    
    def __init__(self, course_id, name, teacher):
        self.id = course_id
        self.name = name
        self.teacher = teacher
        self.students = []


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "teacher": self.teacher,
            "students": [
                student.id for student in self.students
            ]
        }
    

    def show_students(self):
        if not self.students:
            print("no student yet!")
            return

        for student in self.students:
            print(student)
    

    def __str__(self):
        return f"{self.id} | {self.name} | {self.teacher}"
    

class SystemManagement:

    def __init__(self):
        self.students = []
        self.courses = []

        self.next_student_id = 1
        self.next_course_id = 1


    # save/load

    def save_data(self):

        data = {
            "students": [student.to_dict() for student in self.students],
            "courses": [course.to_dict() for course in self.courses]
        }

        with open("students_data.json", "w") as file:
            json.dump(data, file, indent=4)


    def load_data(self):

        try:

            with open("students_data.json", "r") as file:
                data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return
        
        self.students.clear()
        self.courses.clear()

        for student_data in data["students"]:

            student = Student(
                student_data["id"],
                student_data["name"],
                student_data["student_class"]
            )

            self.students.append(student)

        for course_data in data["courses"]:

            course = Course(
                course_data["id"],
                course_data["name"],
                course_data["teacher"]
            )

            self.courses.append(course)

        for student_data in data["students"]:

            found_student = helpers.find_by_id(self.students, student_data["id"])

            for course_id in student_data["courses"]:

                found_course = helpers.find_by_id(self.courses, course_id)

                if found_course:
                    found_student.courses.append(found_course)

        for course_data in data["courses"]:

            found_course = helpers.find_by_id(self.courses, course_data["id"])

            for student_id in course_data["students"]:

                found_student = helpers.find_by_id(self.students, student_id)

                if found_student:
                    found_course.students.append(found_student)


        # manage next id

        if self.students:
            self.next_student_id = max(student.id for student in self.students) + 1

        if self.courses:
            self.next_course_id = max(course.id for course in self.courses) + 1


    # core methods

    def add_student(self):

        name = helpers.get_non_empty_input("student's name: ")
        class_name = helpers.get_non_empty_input("class name: ")
        
        existing_student = helpers.find_student_by_name_and_class(
            self.students,
            name,
            class_name
        )

        if existing_student:
            print(f"{existing_student.name} in {existing_student.class_name} already exists!")
            return
        
        new_student = Student(self.next_student_id, name, class_name)
        
        self.students.append(new_student)

        self.next_student_id += 1

        print(f"{new_student.name} added successfully as student!")


    def show_students(self):

        if not self.students:
            print("no student found!")
            return
        
        for student in self.students:
            print(student)
            student.show_courses()
            print("-" * 40)


    def search_student(self):

        query = helpers.get_non_empty_input("search: ", "please enter student's id or name!")

        if query.isdigit():

            found_student = helpers.find_by_id(self.students, int(query))

            if found_student:
                helpers.show_student_details(found_student)

            else:
                print("no student found!")
            
        else:
            found_students = helpers.find_by_name(self.students, query)

            if found_students:

                for student in found_students:
                    helpers.show_student_details(student)

            else:
                print("no student found!")


    def delete_student(self):

        name = helpers.get_non_empty_input(
            "enter student's name want to remove: ",
            "please enter a student name!"
        ).lower()
        
        result = helpers.find_by_name(self.students, name)

        if not result:
            print("no student found!")
            return
        
        for student in result:
            print(student)

        student_id = helpers.get_valid_number(
            "enter student's id to remove: ",
            "invalid id! please try again."
        )
        
        found_student = helpers.find_by_id(self.students, student_id)

        if not found_student:
            print("no student found!")
            return
        
        for course in found_student.courses:

            if found_student in course.students:
                course.students.remove(found_student)

        deleted = helpers.delete_item_by_id(self.students, int(student_id))

        if deleted:
            print(f"{found_student.name} deleted successfully!")
            return
        
        else:
            print("no student found to delete!")


    def add_course(self):

        name = helpers.get_non_empty_input("course's name: ")
        teacher = helpers.get_non_empty_input("teacher's name: ")
        
        existing_course = helpers.find_course_by_name_and_teacher(self.courses, name, teacher)

        if existing_course:
            print(f"{existing_course.name} already exists!")
            return
        
        new_course = Course(self.next_course_id,name, teacher)

        self.courses.append(new_course)

        self.next_course_id += 1

        print(f"{new_course.name} added successfully!")


    def show_courses(self):

        if not self.courses:
            print("no course found!")
            return
        
        for course in self.courses:
            print(course)
            course.show_students()
            print("-" * 40)


    def search_course(self):

        query = helpers.get_non_empty_input(
            "enter course's id or name: ",
            "please enter course's id or name!"
        )
        
        if query.isdigit():

            found_course = helpers.find_by_id(self.courses, int(query))

            if found_course:
                helpers.show_course_details(found_course)

            else:
                print("no course found!")

        else:

            found_courses = helpers.find_by_name(self.courses, query)

            if found_courses:

                for course in found_courses:
                    helpers.show_course_details(course)

            else:
                print("no course found!")


    def delete_course(self):

        name = helpers.get_non_empty_input(
            "enter course's name want to remove: ",
            "please enter a course's name!"
        )
            
        found_course = helpers.find_by_name(self.courses, name)

        if not found_course:
            print("no course found!")
            return
            
        for course in found_course:
            print(course)

        course_id = helpers.get_valid_number(
            "enter course's id to remove: ",
            "invalid id! please try again."
        )
            
        found_course = helpers.find_by_id(self.courses, course_id)

        if not found_course:
            print("no course found!")
            return
            
        for student in found_course.students:

            if found_course in student.courses:
                student.courses.remove(found_course)

        deleted = helpers.delete_item_by_id(self.courses, int(course_id))

        if deleted:
            print(f"{found_course.name} deleted successfully!")
        else:
            print("no course found to delete!")


    # relationship methods

    def enroll_student(self):

        student_name = helpers.get_non_empty_input("enter student's name: ")
        class_name = helpers.get_non_empty_input("enter class's name: ")

        course_name = helpers.get_non_empty_input("enter course's name: ")
        teacher_name = helpers.get_non_empty_input("enter teacher's name: ")
        
        found_student = helpers.find_student_by_name_and_class(
            self.students,
            student_name,
            class_name
        )

        found_course = helpers.find_course_by_name_and_teacher(
            self.courses,
            course_name,
            teacher_name
        )

        if not found_student:
            print("no student found!")
            return
        
        if not found_course:
            print("no course found!")
            return
        
        if found_course in found_student.courses:
            print(f"{found_student.name} already enrolled!")
            return
        
        found_student.courses.append(found_course)
        found_course.students.append(found_student)

        print(f"{found_student.name} enrolled successfully!")


    def unenroll_student(self):

        student_name = helpers.get_non_empty_input("enter student's name: ")
        class_name = helpers.get_non_empty_input("enter class's name: ")

        course_name = helpers.get_non_empty_input("enter course's name: ")
        teacher_name = helpers.get_non_empty_input("enter teacher's name: ")
        
        found_student = helpers.find_student_by_name_and_class(
            self.students,
            student_name,
            class_name
        )
        found_course = helpers.find_course_by_name_and_teacher(
            self.courses,
            course_name,
            teacher_name
        )

        if not found_student:
            print("no student found!")
            return
        
        if not found_course:
            print("no course found!")
            return
        
        if found_student not in found_course.students:
            print(f"{found_student.name} not enrolled before!")
            return
        
        found_student.courses.remove(found_course)
        found_course.students.remove(found_student)

        print(f"{found_student.name} unenrolled successfully!")

