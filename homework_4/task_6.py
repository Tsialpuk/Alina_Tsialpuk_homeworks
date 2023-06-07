"""
Заполнить список степенями числа 2 (от 2степ1 до 2 степ N)
не самим создавать такой список, а сделать так,
чтобы ваша программа сгенерировала сама такой список.
Почитать про генератор списков
"""
while True:
    num1 = float(input('введите число от 1 до 10:'))
    str1 = input('введите цвет (красный или черный):')
    num2
    if operation == '0':
        print('принудительная остановка')
        break
    elif operation == "+":
        print(num1+num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "/":
        if num2 == 0:
            print('на ноль делить нельзя')
        else:
            print(num1/num2)