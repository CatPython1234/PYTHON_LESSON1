num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))
operator = input('operator: ')

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '//':
    print(num1 // num2)
else:
    print('EROR')

print('END')