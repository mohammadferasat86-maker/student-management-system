import numpy as np

def merge(a, b) :
    r = []
    i = 0
    j = 0
    while(i < len(a) and j < len(b)) :
        if a[i] > b[j] :
            r.append(b[j])
            j +=1
        else :
            r.append(a[i])
            i += 1
    r += a[i:] + b[j:]
    return r

def merge_sort(a) :
    if len(a) <= 1 :
        return a 
    return merge(merge_sort(a[: len(a) // 2]), merge_sort(a[len(a) // 2 :]))
    
class dars :
    def __init__(self, name, id, vahed) :
        self.name = name
        self.__id = id
        self.vahed = vahed

    @property
    def id(self) :
        return self.__id

class person :
    def __init__(self, name, age, codemeli) :
        self.name = name
        self.age = age
        self.__codemeli = codemeli

    @property
    def codemeli(self) : 
        return self.__codemeli

class student(person) : 
    def __init__(self, name, age, codemeli, student_id):
        super().__init__(name, age, codemeli)
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, dars, grade):
        self.grades[dars.id] = {
            "grade": grade,
            "vahed": dars.vahed   
        }
    def units_num(self) :
        if self.grades == {} :
            return 0.0
        num = 0
        for d in self.grades.values() : 
            num += d["vahed"]
        return num
    
    def moadel(self) :
        if self.grades == {} :
            return 0.0
        sum = 0
        for d in self.grades.values() : 
            sum += d["grade"] * d["vahed"]
        return sum / self.units_num()

    def info(self) :
        print(f"Name: {self.name}, codemeli: {self.codemeli}, Age: {self.age}, student id: {self.student_id}")

    def karname(self) :
        self.info()
        print("nomarat :")
        for k, v in self.grades.items() :
            print(k)
            print(v)

        print(f"moadel : {self.moadel()}")

class modiriyat : 
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, new_student):
        self.students[new_student.student_id] = new_student

    def add_course(self, new_course):
        self.courses[new_course.id] = new_course

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            raise ValueError(f"there is no student with {student_id} id")
        
    def add_student_grade(self, student_id, dars_id, grade):
        if student_id not in self.students:
            raise ValueError(f"there is no student with {student_id} id")
        if dars_id not in self.courses:
            raise ValueError(f"there is no course with {dars_id} id")
        s = self.students[student_id]
        d = self.courses[dars_id]
        s.add_grade(d, grade)

    def karname(self, student_id):
        if student_id in self.students:
            s = self.students[student_id]
            s.karname()
        else:
            raise ValueError(f"there is no student with {student_id} id")

    def sort_students_by_name(self) :
        s_list = []
        for s in self.students.values():
            a = (s.name, s.student_id, s)
            s_list.append(a)
        s_list = merge_sort(s_list)
        return s_list

    def sort_students_by_avrage_grade(self) :
        s_list = []
        for s in self.students.values():
            a = (s.moadel(), s.student_id, s)
            s_list.append(a)
        s_list = merge_sort(s_list)
        return s_list
    
    def sort_students_by_number_of_units(self) :
        s_list = []
        for s in self.students.values():
            a = (s.units_num(), s.student_id, s)
            s_list.append(a)
        s_list = merge_sort(s_list)
        return s_list
    
    def show_student_statistics(self) :
        gs_list = []
        for s in self.students.values():
            gs_list.append(s.moadel())
        ags = np.mean(gs_list)
        print(f"میانگین معدل دانشجویان = {ags}")
        mgs = np.median(gs_list)
        print(f"میانه معدل دانشجویان = {mgs}")
        sgs = np.std(gs_list)
        print(f"انحراف میار معدل دانشجویان = {sgs}")
        vgs = np.var(gs_list)
        print(f"واریانس معدل دانشجویان = {vgs}")
        s = len(gs_list)
        gs_list = np.array(gs_list)
        fs = np.sum(gs_list < 12)
        print(f" دانشجو مشروط شده اند{s}دانشجو از{fs}")

system = modiriyat()

print("""guide :
(n = number of students and m = number of courses) 
(پیچیدگی زمانی هر عملیات رو به روی آن داخل پرانتز نوشته شده) 

add student (1) 
add course (1) 
remove student (1) 
add student grades (1) 
student info (1) 
student report (m)
sort students by name (nlog(n)) 
sort students by avrage grade (mn + nlog(n)) 
sort students by number of units (nm + nlog(n)) 
show student statistics (nm)
show students(n)
show courses(m)
end """)

while True:
    c = input("\nEnter command: ").strip().lower()
    if c == "add student":
        name = input("name: ")
        age = int(input("age: "))
        codemeli = input("national id: ")
        student_id = int(input("student id: "))
        new_student = student(name, age, codemeli, student_id)
        system.add_student(new_student)
        print("student added")

    elif c == "add course":
        name = input("name: ")
        course_id = int(input("id: "))
        vahed = int(input("units: "))
        new_course = dars(name, course_id, vahed)
        system.add_course(new_course)
        print("course added")

    elif c == "remove student":
        student_id = int(input("student id: "))
        system.remove_student(student_id)
        print("student removed")

    elif c == "add student grade":
        student_id = int(input("student id: "))
        course_id = int(input("course id: "))
        grade = float(input("grade: "))
        if grade < 0 or grade > 20:
            raise ValueError("grade must be between 0 and 20")
        system.add_student_grade(student_id, course_id, grade)
        print("grade added")

    elif c == "student info":
        student_id = int(input("student id: "))
        if student_id not in system.students:
            raise ValueError(f"There is no student with {student_id} id")
        system.students[student_id].info()

    elif c == "student report":
        student_id = int(input("student id: "))
        system.karname(student_id)

    elif c == "sort students by name":
        ss = system.sort_students_by_name()
        for n, s_id, s in ss:
            s.info()

    elif c == "sort students by average grade":
        ss = (system.sort_students_by_avrage_grade())
        for n, s_id, s in ss:
            print(f"name: {s.name}, student id: {s.student_id}, average: {n}")

    elif c == "sort students by number of units":
        ss = (system.sort_students_by_number_of_units())
        for n, s_id, s in ss:
            print(f"name: {s.name}, student id: {s.student_id}, Units: {n}")

    elif c == "show student statistics":
        if not system.students:
            print("there are no students")
            continue
        system.show_student_statistics()

    elif c == "show students":
        for s in system.students.values():
            s.info()

    elif c == "show courses":
        for course in system.courses.values():
            print(f"name: {course.name}, id: {course.id}, units: {course.vahed}")

    elif c == "end":
        break

    else:
        print("invalid command !")

""" test case :
add student
Ali Rezaei
20
0011223344
40424501
add student
Sara Ahmadi
30
0099887766
40424502
add student
Reza Karimi
21
0055443322
40424503
add course
Math1
101
3
add course
Physics1
102
4
add course
Programming
103
3
add student grade
40424501
101
18.5
add student grade
40424502
102
16
add student grade
40424501
103
19
add student grade
40424502
101
14
add student grade
40424502
102
17.5
add student grade
40424503
101
9.5
add student grade
40424503
103
11
student info
40424501
student report
40424502
sort students by name
sort students by average grade
sort students by number of units
show student statistics
show students
show courses
remove student
40424502
show students
somegarbagecommand
end
"""


""" گزارش پروژه :


"""