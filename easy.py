import math


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    a = str(number)
    b = a.split('.')
    result1 = b[1][0:ndigits]
    result2 = b[1][ndigits:ndigits+1]
    if int(result2) > ndigits:
        result1 = int(result1) + 1
        if len(str(result1)) > ndigits:
            b[0] = int(b[0]) + 1
            b[0] = str(b[0])
            result1 = 0
    result = (b[0] + '.' + str(result1))
    result = float(result)
    return result


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def happy_number(num):
    s_one = 0
    s_two = 0
    strNum = str(num)
    nums = len(strNum) // 2
    for each in strNum[:nums]:
        s_one = s_one + int(each)
    for each in strNum[-nums:]:
        s_two = s_two + int(each)
    if s_one == s_two:
        return "Число счастливое"
    else:
        return "Число обыкновенное"
print(happy_number(124474412))
