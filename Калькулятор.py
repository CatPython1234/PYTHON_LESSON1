num = int(input('Введите число: '))
num2 = int(input('Введите число: '))
sing = input('Введите знак: ')

if sing == '+':
    print(num + num2)
elif sing == '-':
    print(num - num2)
elif sing == '*':
    print(num * num2)
elif sing == '//':
    print(num // num2)
else:
    print('Eror')

print('END')