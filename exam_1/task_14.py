"""
14.	С клавиатуры вводится десятизначное число.
Вывести на экран четные числа входящие в данное число.
Например 1234567892  2 4 6 8 2
"""
num1 = int(input("Введите десятизначное число:"))
print(num1)
str1 = str(num1)
list2 = []
for i in str1:
    if int(i) % 2 == 0:
        list2.append(i)
print(list2)


