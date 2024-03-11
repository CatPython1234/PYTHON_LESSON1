class Спортсмен:
    def __int__(self,name,age):
        self.name=name
        self.age=age
        print('(Спортсмен: {0})'.format(self.name))
    def tell(self):
        print('Имя:"{0}" Возраст:"{1}" Зарплата:"{2}"'.format(self.name, self.age, self.salary), end=" ")

class Лыжник(Спортсмен):
    def __init__(self,name,age,salary,ski):
        Спортсмен.__int__(self,name,age)
        self.ski=ski
        print('(Лыжник: {0})'.format(self.name))
    def tell(self):
        Спортсмен.tell(self)
        print('Лыжи: "{0:d}"'.format(self.ski))
    def tell(self):
        Спортсмен.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Атлет(Спортсмен):
    def __init__(self,name,age,salary,Yoga_Belt):
            Спортсмен.__int__(self,name,age)
            self.Yoga_Belt=Yoga_Belt
            print('(Атлет: {0})'.format(self.name))
    def tell(self):
            Спортсмен.tell(self)
            print('Ремень_для_йоги: "{0:d}"'.format(self.Yoga_Belt))
    def tell(self):
        Спортсмен.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))


l = Лыжник('Андрей',30,'30000','Лыжи')
a = Атлет('Вова',25,'25000','Пояс для йоги')

print()

members = [l, a]
for members in members:
    members.tell()
