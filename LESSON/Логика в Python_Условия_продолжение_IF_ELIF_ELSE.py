num1 = int(input('Введите число: '))

if num1 > 10 and num1 % 2 == 0:
    print('Число больше 10 и четное')
elif num1 % 2 != 0:
    print('Число нечетное')
elif num1 == 8:
    print('Вы ввели 8')
else:
    print('ПОКА')

print('КОНЕЦ')