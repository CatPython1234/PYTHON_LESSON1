
a = 1 + 2 # сложение
b = 20 - 2 # вычитание
c =  3 * 3 # умножение
d = 5 // 2 # //-деление вернет int-целое число
print(d, type(d))
e = 5 / 2 # /-деление вернет float
print(e, type(e))
f = 5 % 2 # %-деление вернет int-остаток-1
print(f, type(f))

j = 5**3 # возведение в степень
print(j,type(j))

num1 = -142
abs_num = abs(num1)# Модуль уберает минус - было -142,стало 142
print(abs_num)


num2 = -142
print(abs(num2))

num2  = "hello"
print(num2)

# тип данных:str - str() тип данных:float - float() тип данных:int - int()
num3 = 25 # 25-число-int
num3 = str(num3) # '25'-строка-str
num4 = float(num3)
print(num3,type(num3)) # 25 <class 'str'>
print(num4,type(num4)) # 25.0 <class 'float'>

num5 = int(input('Введите число 1: '))
num6 = int(input('Введите число 2: '))
print(num5 + num6, 'Сложили числа')


#print(5 / 0)-делить на 0 нельзя


