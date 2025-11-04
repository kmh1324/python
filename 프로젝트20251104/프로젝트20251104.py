##import temp
##
##c_temp = int(input("섭씨 입력: "))
##f_temp = int(input("화씨 입력: "))
##
##print(temp.c_to_f(c_temp))
##print(temp.f_to_c(f_temp))


##class Student:
##    def __init__(self, name, korean, math, english, science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##
##    def get_sum(self):
##        return self.korean + self.math + self.english + self.science
##
##    def get_average(self):
##        return self.get_sum() / 4
##
##    def to_string(self):
##        return "{}\t{}\t{}".format(\
##            self.name,\
##            self.get_sum(),\
##            self.get_average())
##
##students = [
##    Student("윤인성", 87, 98, 88, 95),
##    Student("연하진", 92, 98, 96, 98),
##    Student("구지연", 76, 96, 94, 90),
##    Student("나선주", 98, 92, 96, 92),
##    Student("윤아린", 95, 98, 98, 98),
##    Student("윤멸월", 64, 88, 92, 92)
##]
##
##print("이름", "총점", "평균", sep = "\t")
##for student in students:
##    print(student.to_string())


##class Student:
##    def study(self):
##        print("공부를 합니다.")
##
##class Teacher:
##    def teach(self):
##        print("학생을 가르칩니다.")
##
##classroom = [Student(), Student(), Teacher(), Student(), Student()]
##
##for person in classroom:
##    if isinstance(person, Student):
##        person.study()
##    elif isinstance(person, Teacher):
##        person.teach()


##class Student:
##    def __init__(self, name, korean, math, english, science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##
##    def get_sum(self):
##        return self.korean + self.math + self.english + self.science
##
##    def get_average(self):
##        return self.get_sum() / 4
##
##    def __str__(self):
##        return "{}\t{}\t{}".format(
##            self.name,
##            self.get_sum(),
##            self.get_average())
##
##students = [
##    Student("윤인성", 87, 98, 88, 95),
##    Student("연하진", 92, 98, 96, 98),
##    Student("구지연", 76, 96, 94, 90),
##    Student("나선주", 98, 92, 96, 92),
##    Student("윤아린", 95, 98, 98, 98),
##    Student("윤멸월", 64, 88, 92, 92)
##]
##
##print("이름", "총점", "평균", sep = "\t")
##for student in students:
##    print(str(student))
    

##class Student:
##    def __init__(self, name, korean, math, english, science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##
##    def get_sum(self):
##        return self.korean + self.math + self.english + self.science
##
##    def get_average(self):
##        return self.get_sum() / 4
##
##    def __str__(self):
##        return "{}\t{}\t{}".format(
##            self.name,
##            self.get_sum(),
##            self.get_average())
##
##    def __eq__(self, value):
##        return self.get_sum() == value.get_sum()
##    def __ne__(self, value):
##        return self.get_sum() != value.get_sum()
##    def __gt__(self, value):
##        return self.get_sum() > value.get_sum()
##    def __ge__(self, value):
##        return self.get_sum() >= value.get_sum()
##    def __lt__(self, value):
##        return self.get_sum() < value.get_sum()
##    def __le__(self, value):
##        return self.get_sum() <= value.get_sum()
##
##students = [
##    Student("윤인성", 87, 98, 88, 95),
##    Student("연하진", 92, 98, 96, 98),
##    Student("구지연", 76, 96, 94, 90),
##    Student("나선주", 98, 92, 96, 92),
##    Student("윤아린", 95, 98, 98, 98),
##    Student("윤명월", 64, 88, 92, 92)
##]
##
##student_a = Student("윤인성", 87, 98, 88, 95)
##student_b = Student("연하진", 92, 98, 96, 98)
##
##print("student_a == student_b = ", student_a == student_b)
##print("student_a != student_b = ", student_a != student_b)
##print("student_a > student_b = ", student_a > student_b)
##print("student_a >= student_b = ", student_a >= student_b)
##print("student_a < student_b = ", student_a < student_b)
##print("student_a <= student_b = ", student_a <= student_b)

##class Student:
##    count = 0
##
##    def __init__(self, name, korean, math, english, science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##
##        Student.count += 1
##        print("{}번째 학생이 생성되었습니다.".format(Student.count))
##
##students = [
##    Student("윤인성", 87, 98, 88, 95),
##    Student("연하진", 92, 98, 96, 98),
##    Student("구지연", 76, 96, 94, 90),
##    Student("나선주", 98, 92, 96, 92),
##    Student("윤아린", 95, 98, 98, 98),
##    Student("윤명월", 64, 88, 92, 92),
##]
##
##print()
##print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))


##class Student:
##    count = 0
##    students = []
##
##    @classmethod
##    def print(cls):
##        print("------ 학생 목록 ------")
##        print("이름\t총점\t평균")
##        for student in cls.students:
##            print(str(student))
##        print("------ ------ ------")
##
##    def __init__(self, name, korean, math, english, science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##        Student.count += 1
##        Student.students.append(self)
##
##
##    def get_sum(self):
##        return self.korean + self.math + self.english + self.science
##
##    def get_average(self):
##        return self.get_sum() / 4
##
##    def __str__(self):
##        return "{}\t{}\t{}".format(\
##            self.name,\
##            self.get_sum(),\
##            self.get_average())
##
##Student("윤인성", 87, 98, 88, 95)
##Student("연하진", 92, 98, 96, 98)
##Student("구지연", 76, 96, 94, 90)
##Student("나선주", 98, 92, 96, 92)
##Student("윤아린", 95, 98, 98, 98)
##Student("윤명월", 64, 88, 92, 92)
##Student("김미화", 82, 86, 98, 88)
##Student("김연화", 88, 74, 78, 92)
##Student("박아현", 97, 92, 88, 95)
##Student("서준서", 45, 52, 72, 78)
##
##Student.print()


##class Test:
##    def __init__(self, name):
##        self.name = name
##        print("{} - 생성되었습니다.".format(self.name))
##    def __del__(self):
##        print("{} - 파괴되었습니다.".format(self.name))
##
##
##Test("A")
##Test("B")
##Test("C")


##class Test:
##    def __init__(self, name):
##        self.name = name
##        print("{} - 생성되었습니다.".format(self.name))
##    def __del__(self):
##        print("{} - 파괴되었습니다.".format(self.name))
##
##a = Test("A")
##b = Test("B")
##c = Test("C")


##import math
##
##class Circle:
##    def __init__(self, radius):
##        self.radius = radius
##    def get_circumference(self):
##        return 2 * math.pi * self.radius
##    def get_area(self):
##        return math.pi * (self.radius ** 2)
##
##circle = Circle(10)
##print("원의 둘레:", circle.get_circumference())
##print("원의 넓이:", circle.get_area()) 


import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_
