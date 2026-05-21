

def find_by_id(items, item_id):
    for item in items:
        if item.id == item_id:
            return item
        
    return None


def find_by_name(items, name):

    name = name.lower()

    exact_matches = []
    partial_matches = []

    for item in items:
        if item.name.lower() == name:
            exact_matches.append(item)

        elif name in item.name.lower():
            partial_matches.append(item)

    return exact_matches + partial_matches
    

def find_student_by_name_and_class(students, student_name, student_class):
    for student in students:
        if (
            student.name.lower() == student_name.lower()
            and
            student.student_class.lower() == student_class.lower()
        ):
            return student
    return None


def find_course_by_name_and_teacher(courses, course_name, teacher):

    for course in courses:

        if (
            course.name.lower() == course_name.lower()
            and
            course.teacher.lower() == teacher.lower()
        ):
            return course
        
    return None
    

def delete_item_by_id(items, item_id):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return True
        
    return False


def get_non_empty_input(message, error_message="this field is required!"):

    while True:

        value = input(message).strip()

        if value:
            return value
        
        print(error_message)


def show_student_details(student):

    print(student)
    student.show_courses()


def show_course_details(course):

    print(course)
    course.show_students()


def get_valid_number(message, error_message="please enter a valid number!"):

    value = input(message).strip()

    if value.isdigit():
        return int(value)
    
    print(error_message)