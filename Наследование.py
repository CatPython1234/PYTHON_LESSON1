'''
(Создан SchoolMember: Mrs. Shrividya)
(Создан Teacher: Mrs. Shrividya)
(Создан SchoolMember: Swaroop)
(Создан Student: Swaroop)

Имя:"Mrs.Shrividya" Возраст:"40" Зарплата: "30000"
Имя:"Swaroop" Возраст:"15" Оценки: "5"
'''
class SchoolMembler:
    def __int__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMembler):
    def __init__(self, name, age, salary):
        SchoolMembler.__int__(self,name,age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMembler.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMembler):
    def __init__(self, name, age, marks):
        SchoolMembler.__int__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        SchoolMembler.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 15, 5)

print()

members = [t, s]
for members in members:
    members.tell()