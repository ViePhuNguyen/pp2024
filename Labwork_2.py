
class Student:
    def __init__(self, id_student, name_student, dob_student):
        self.id_student = id_student
        self.name_student = name_student
        self.dob_student = dob_student
        self.marks = {}

    def add_mark(self, course, mark):
        self.marks[course.course_id] = mark

    def display_info(self):
        print(f"ID: {self.id_student}, Name: {self.name_student}, DOB: {self.dob_student}")

    def display_marks(self):
        for course_id, mark in self.marks.items():
            print(f"   Course ID: {course_id}, Mark: {mark}")


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def display_info(self):
        print(f"Course ID: {self.course_id}, Course Name: {self.course_name}")


class function:
    def __init__(self):
        self.students_list = []
        self.courses_list = []

    def add_student(self, student):
        self.students_list.append(student)

    def add_course(self, course):
        self.courses_list.append(course)

    def display_students(self):
        for student in self.students_list:
            student.display_info()

    def display_courses(self):
        for course in self.courses_list:
            course.display_info()

    def input_marks(self):
        course_id = input("Enter the Course ID for which you want to input marks: ")

        for student in self.students_list:
            mark = input(f"Enter the mark for {student.name_student} in {course_id}: ")
            course = next((c for c in self.courses_list if c.course_id == course_id), None)
            if course:
                student.add_mark(course, mark)
            else:
                print(f"Course with ID {course_id} not found.")

    def display_marks(self):
        for student in self.students_list:
            student.display_info()
            student.display_marks()



Function = function()

student_num = int(input("How many students you want to add: "))
for i in range(student_num):
    id_input = input("Student ID: ")
    name_input = input("Student Name: ")
    dob_input = input("Date of Birth DD/MM/YY: ")

    student = Student(id_input, name_input, dob_input)
    function.add_student(student)

course_num = int(input("How many courses do you want to add: "))
for i in range(course_num):
    course_id_input = input("Course ID: ")
    course_name_input = input("Course Name: ")

    course = Course(course_id_input, course_name_input)
    function.add_course(course)
#Display student information and course
function.display_students()
function.display_courses()
#Input mark and display
function.input_marks()
function.display_marks()
