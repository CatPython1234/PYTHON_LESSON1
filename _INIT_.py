class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print("HELLO, My NAME", self.name)

p = Person('ROMAN')
p.say_hi()