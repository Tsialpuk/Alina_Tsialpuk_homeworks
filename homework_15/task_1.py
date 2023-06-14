"""
1)	Простейший калькулятор c введёнными двумя числами вещественного типа.
Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями. Обработать ошибку:
“Деление на ноль”
Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
"""

def sum():
    return x + y
def raznica():
    return x - y
def proizv():
    return x * y
def delenie():
    return x / y

while True:
    x = float(input('Введите первое вещественное число'))
    y = float(input('введите второе вещественное число'))
    operation = input('Введите операцию (+, -, *, /, 0) : ')
    if operation == '0':
        print("Программа завершена!")
        break
    elif operation == str('+'):
        print(sum())
    elif operation == '-':
        print(raznica())
    elif operation == '*':
        print(proizv())
    elif operation == '/':
        try:
            print(delenie())
        except ZeroDivisionError:  # перехватываем ошибку и перераспределяем ее
            print('На ноль делить нельзя! Введите другое число или выберите другую операцию!')



