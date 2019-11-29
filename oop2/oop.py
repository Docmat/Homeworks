class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, salary):
        self.salary = salary

    def tell(self, salary):
        return self.salary


class Student(SchoolMember):
    def __init__ (self,marks):
        self.marks = marks

    def tell(self,marks):
        return self.marks


sm = SchoolMember("Daniyar", 26)
print(sm.name)

teacher = Teacher(30000)
print(teacher.salary)

student = Student(5)
print(student.marks)
