# bool - True(1) и Fals(0)

num1 = int(input('Введите число: ')) # 11
# 11 > 10-True AND 11 % 2-False#
#True and False - 1 * 0 = 0-False


usl1 = num1 > 10 and num1 % 2 == 0 # Если num1 больше 10 и при этом num % 2 равен 0
print(usl1)
#10 > 5 - True
#10 > 10 - False
#10 >= 10 - True
#10 < 10 - False
#10 <= 10 - True
#10 == 10 - 10=10 - True
#10 == 9 - 10=9 - False
#10 != 9 - 10 "не != равно" 9 - True
#and - И (*)
#or - ИЛИ (+)#

usl2 = num1 < 10 and num1 % 2 == 0 # 9 < 10 - True and 9 % 2 - False -> 1 * 0 = 0-False
print(usl2)



#usl1 = num1 > 10 and num1 % 2 == 0 (12 > 10 - True and 12 % 2 - True -> 1 * 1 = 1-True
usl2 = num1 < 10 and num1 % 2 == 0





usl3 = num1 % 3 == 0 or num1 > 100 # 50 % 3 - False or(+) 50>100 - False -> 0+0 = 0-False
print(usl3)


#usl3 = num1 % 3 == 0 or num1 > 100 (66 % 3 - True or(+) 66>100 - False -> 1+0 = 1-True


#if условие == True:
# действие
# elif(иначе) условие == True:
# действие
# elif-может быть сколько угодно:
# else:
# действие(если не одно условие не сработало)#

