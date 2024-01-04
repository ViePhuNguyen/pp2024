""""                                            ///Problem breakdown///
Input   
        - Numbers of student in class (the size of list for initial input) 
            //if want fix the numbers of student using tuple or not using list instead
            + Student infor : "ID" , "Name" , "DoB" (using class) 
        - Numbers of courses (list also)
            + Courses information "ID" and "Name" 
                   
        - Select a course and input the mark for student in course
Output - Show the courses
       - Show the list students
       - Show mark of student in given course
"""




class StudentClass:
    def __init__(self, id_student, name_student, dob_student):
        self.id_student     = id_student
        self.name_student   = name_student
        self.dob_student    = dob_student
        self.marks = {}

    def add_mark(self, course, mark):
        self.marks[course.course_id] = mark


students_list   = [] 
student_num     = int(input("How many students you want to add: "))


for i in range(student_num):
    id_input    = input("Student ID: ")
    name_input  = input("Student Name: ")
    dob_input   = input("Date of Birth DD/MM/YY: ")

    student = StudentClass(id_input, name_input, dob_input)
    students_list.append(student)


def student_display():
    for student in students_list:
        print(f"ID: {student.id_student}, Name: {student.name_student}, DOB: {student.dob_student}")





class CourseClass:
    def __init__(self, course_id, course_name):
        self.course_id   = course_id
        self.course_name = course_name

courses_list = [] 
course_num = int(input("How many courses do you want to add: "))

for i in range(course_num):
    course_id_input   = input("Course ID: ")
    course_name_input = input("Course Name: ")

    course = CourseClass(course_id_input, course_name_input)
    courses_list.append(course)

def course_display():
    for course in courses_list:
        print(f"Course ID: {course.course_id}, Course Name: {course.course_name}")




def mark_input():
    course_id = input("Enter the Course ID for which you want to input marks: ")
    for student in students_list:
        mark = input(f"Enter the mark for {student.name_student} in {course_id}: ")
        course = next((c for c in courses_list if c.course_id == course_id), None)
        if course:
            student.add_mark(course, mark)
        else:
            print(f"Course with ID {course_id} not found.")


def mark_display():
    for student in students_list:
        print(f"Student ID: {student.id_student}, Name: {student.name_student}, DOB: {student.dob_student}")
        for course_id, mark in student.marks.items():
            print(f"   Course ID: {course_id}, Mark: {mark}")


#có thể dùng while loop để sử dụng case chọn từng trường hợp , về cơ bản test chức năng input output đều ổn 
def _main_():         
    mark_input()
    mark_display()

_main_()    
    