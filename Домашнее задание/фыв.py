class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))

    def saHI(self):
        print('HELLO, My name {0}.'.format(self.name))

    def howMany():
        print('у нас {0:d} роботов.'.format(Robot.population))

    howMany= staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.saHI()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.saHI()
Robot.howMany()

print("\nfeiefiwejfwef.\n")
print("\nРоботы подняли руку\n")
print("\nРоботы крикнули\n")

print("Robot destroer")
del droid1
del droid2

Robot.howMany()