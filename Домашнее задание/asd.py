class Sportsman:
    def __int__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан Спортсмен: {0})'.format(self.name))
    def tell(self):
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Skier(Sportsman):
    def __init__(self, name, age, salary):
        Sportsman.__int__(self,name,age)
        self.salary = salary
        print('(Создан Лыжник: {0})'.format(self.name))

    def tell(self):
        Sportsman.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Athlete(Sportsman):
    def __init__(self, name, age, weight):
        Sportsman.__int__(self, name, age)
        self.weight = weight
        print('(Создан Атлет: {0})'.format(self.name))

    def tell(self):
        Sportsman.tell(self)
        print('Вес: "{0:d}"'.format(self.weight))


t = Skier('Андрей', 40, 30000)
s = Athlete('Вова', 35, 12)

print()

members = [t, s]
for members in members:
    members.tell()