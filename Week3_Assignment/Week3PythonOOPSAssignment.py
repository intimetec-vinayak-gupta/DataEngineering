class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
    
    def register_student(self, student):
        if student in self.students:
            print(f"{student.name} is already registered at {self.name}.")
            return False
        
        self.students.append(student)
        print(f"{student.name} has been registered at {self.name}.")
        return True
    
    def offer_course(self, course):
        for existing_course in self.courses:
            if existing_course.course_code == course.course_code:
                print(f"Course {course.course_code} is already offered at {self.name}.")
                return False
        
        self.courses.append(course)
        print(f"Course {course.course_code}: {course.course_name} is now offered at {self.name}.")
        return True
    
    def get_students_by_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                return [student.name for student in course.enrolled_students]
        
        print(f"Course {course_code} not found at {self.name}.")
        return []
    
    # Dunder/Magic methods
    def __str__(self):
        return f"University: {self.name} ({len(self.students)} students, {len(self.courses)} courses)"
    
    def __repr__(self):
        return f"University(name='{self.name}', students={len(self.students)}, courses={len(self.courses)})"
    
    def __len__(self):
        return len(self.students)

class Course:
    def __init__(self, course_code, course_name, max_students):
        self.course_code = course_code
        self.course_name = course_name
        self.max_students = max_students
        self.enrolled_students = []
        
    def enroll_student(self, student):
        if(len(self.enrolled_students) >= self.max_students):
            print(f"Cannot enroll {student.name} in {self.course_code}: Course is full.")
            return
        if(student in self.enrolled_students):
            print(f"{student.name} is already enrolled in {self.course_code}.")
            return
        
        self.enrolled_students.append(student)
        student.courses_enrolled.append(self)
        print(f"{student.name} has been enrolled in {self.course_code}.")
        
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses_enrolled = []
        
    def enroll_course(self, course):
        if(len(course.enrolled_students) >= course.max_students):
            print(f"Cannot enroll {self.name} in {course.course_code}: Course is full.")
            return
        if(course in self.courses_enrolled):
            print(f"{self.name} is already enrolled in {course.course_code}.")
            return
        
        course.enrolled_students.append(self)
        self.courses_enrolled.append(course)
        print(f"{self.name} has been enrolled in {course.course_code}.")


if __name__ == "__main__":
    
    my_university = University("Delhi University")
    print(f"Created: {my_university}")
    
    math_course = Course("MATH101", "Mathematics", 3)
    english_course = Course("ENG101", "English Literature", 2)
    science_course = Course("SCI101", "General Science", 4)
    
    my_university.offer_course(math_course)
    my_university.offer_course(english_course)
    my_university.offer_course(science_course)
    
    rahul = Student(101, "Rahul Sharma", 19)
    priya = Student(102, "Priya Singh", 20)
    amit = Student(103, "Amit Kumar", 18)
    kavya = Student(104, "Kavya Patel", 21)
    arjun = Student(105, "Arjun Reddy", 19)
    
    my_university.register_student(rahul)
    my_university.register_student(priya)
    my_university.register_student(amit)
    my_university.register_student(kavya)
    my_university.register_student(arjun)
    
    rahul.enroll_course(math_course)
    rahul.enroll_course(english_course)
    
    priya.enroll_course(math_course)
    priya.enroll_course(science_course)
    
    amit.enroll_course(math_course)  # Math course will be full now
    amit.enroll_course(science_course)
    
    kavya.enroll_course(math_course)  # This should fail - course full
    kavya.enroll_course(english_course)
    
    arjun.enroll_course(science_course)
    arjun.enroll_course(english_course)  # This should fail - course full
    
    math_students = my_university.get_students_by_course("MATH101")
    english_students = my_university.get_students_by_course("ENG101")
    science_students = my_university.get_students_by_course("SCI101")
    
    print(f"Math class students: {math_students}")
    print(f"English class students: {english_students}")
    print(f"Science class students: {science_students}")
    
    