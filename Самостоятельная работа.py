class Elevator:
    people_lifted = 0

    def __init__(self, name):
        self.name = name
        self.people_lifted = 0
    def tell(self):
        print('(Создан лифт, который едет вверх)'.format(self.name))

    def lift(self):
        print("{} lifted someone".format(self.name))
        self.people_lifted += 1
        Elevator.people_lifted += 1

    def info(self):
        print(self.name, "lifted", self.people_lifted, "people out of", Elevator.people_lifted)
e = Elevator('Лифт' )
e.tell()
e.lift()